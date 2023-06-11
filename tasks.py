# -*- coding: utf-8 -*-

import os
import shlex
import shutil
import sys
import datetime
from pathlib import Path

from invoke import task
from invoke.main import program
from pelican import main as pelican_main
from pelican.server import ComplexHTTPRequestHandler, RootedHTTPServer
from pelican.settings import DEFAULT_CONFIG, get_settings_from_file

OPEN_BROWSER_ON_SERVE = True
SETTINGS_FILE_BASE = "pelicanconf.py"
SETTINGS = {}
SETTINGS.update(DEFAULT_CONFIG)
LOCAL_SETTINGS = get_settings_from_file(SETTINGS_FILE_BASE)
SETTINGS.update(LOCAL_SETTINGS)

CONFIG = {
    "settings_base": SETTINGS_FILE_BASE,
    "settings_publish": "publishconf.py",
    # Output path. Can be absolute or relative to tasks.py. Default: 'output'
    "deploy_path": SETTINGS["OUTPUT_PATH"],
    # Remote server configuration
    "ssh_user": "www",
    "ssh_host": "my-ssh-server.localhost",
    "ssh_port": "22",
    "ssh_path": "/var/www",
    # Github Pages configuration
    # .. Remote repository can be different from origin
    "github_pages_remote": "deploy",
    "github_pages_branch": "pages",
    "commit_message": (
        f"'Publish site on {datetime.date.today().isoformat()} at {{revision}}'"
    ),
    # Host and port for `serve`
    "host": "localhost",
    "port": 8000,
}


@task
def clean(c):
    """Remove generated files"""
    if os.path.isdir(deploy_path := CONFIG["deploy_path"]):
        print("Removing", deploy_path)
        shutil.rmtree(deploy_path)
        os.makedirs(deploy_path)


@task
def build(c):
    """Build local version of site"""
    pelican_run("-s {settings_base}".format(**CONFIG))


@task
def rebuild(c):
    """`build` with the delete switch"""
    pelican_run("-d -s {settings_base}".format(**CONFIG))


@task
def regenerate(c):
    """Automatically regenerate site upon file modification"""
    pelican_run("-r -s {settings_base}".format(**CONFIG))


@task
def serve(c):
    """Serve site at http://$HOST:$PORT/ (default is localhost:8000)"""

    class AddressReuseTCPServer(RootedHTTPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(
        CONFIG["deploy_path"],
        (CONFIG["host"], CONFIG["port"]),
        ComplexHTTPRequestHandler,
    )

    if OPEN_BROWSER_ON_SERVE:
        # Open site in default browser
        import webbrowser

        webbrowser.open("http://{host}:{port}".format(**CONFIG))

    sys.stderr.write("Serving at {host}:{port} ...\n".format(**CONFIG))
    server.serve_forever()


@task
def reserve(c):
    """`build`, then `serve`"""
    build(c)
    serve(c)


@task
def preview(c):
    """Build production version of site"""
    pelican_run("-s {settings_publish}".format(**CONFIG))


@task
def livereload(c):
    """Automatically reload browser tab upon file modification."""
    from livereload import Server

    def cached_build():
        cmd = "-s {settings_base} -e CACHE_CONTENT=true LOAD_CONTENT_CACHE=true"
        pelican_run(cmd.format(**CONFIG))

    cached_build()
    server = Server()
    theme_path = SETTINGS["THEME"]
    watched_globs = [
        CONFIG["settings_base"],
        "{}/templates/**/*.html".format(theme_path),
    ]

    content_file_extensions = [".html", ".md", ".rst"]
    for extension in content_file_extensions:
        content_glob = "{0}/**/*{1}".format(SETTINGS["PATH"], extension)
        watched_globs.append(content_glob)

    static_file_extensions = [".css", ".js"]
    for extension in static_file_extensions:
        static_file_glob = "{0}/static/**/*{1}".format(theme_path, extension)
        watched_globs.append(static_file_glob)

    for glob in watched_globs:
        server.watch(glob, cached_build)

    if OPEN_BROWSER_ON_SERVE:
        # Open site in default browser
        import webbrowser

        webbrowser.open("http://{host}:{port}".format(**CONFIG))

    server.serve(host=CONFIG["host"], port=CONFIG["port"], root=CONFIG["deploy_path"])


@task(preview)
def rsync_upload(c):
    """Publish via rsync+ssh"""
    c.run(
        "rsync --delete --exclude '.DS_Store' -pthrvz -c "
        "-e 'ssh -p {ssh_port}' "
        "{} {ssh_user}@{ssh_host}:{ssh_path}".format(
            CONFIG["deploy_path"].rstrip("/") + "/", **CONFIG
        )
    )


@task(preview)
def gh_pages(c):
    """Publish to GitHub Pages"""
    if "{revision}" in (commit_message_template := CONFIG["commit_message"]):
        git_id = c.run("git id", hide="out").stdout.strip()
        CONFIG["commit_message"] = commit_message_template.format(
            revision=f"ashwinvis/website@{git_id}"
        )

    c.run("git fetch {github_pages_remote} {github_pages_branch}".format(**CONFIG))
    c.run(
        "ghp-import -r {github_pages_remote} -b {github_pages_branch} "
        "-m {commit_message} "
        "{deploy_path} -p".format(**CONFIG)
    )
    c.run("git push -u {github_pages_remote} {github_pages_branch}".format(**CONFIG))


@task
def cname(c):
    """Write CNAME file"""
    from pelican_ashwinvis import SITEURL

    with open("{deploy_path}/CNAME".format(**CONFIG), "w") as fp:
        fp.write(SITEURL)


@task
def pip_compile(c):
    """Generate from requirements/*.in => requirements/*.txt files"""
    _run_pip_compile(c, "main")
    _run_pip_compile(c, "dev")


def _run_pip_compile(c, prefix):
    c.run(
        "pip-compile -U --resolver=backtracking "
        f"requirements/{prefix}.in -o requirements/{prefix}.txt"
    )
    reqts_txt = Path("requirements", f"{prefix}.txt")

    contents = reqts_txt.read_text()
    contents_rel_path = contents.replace("file://" + os.getcwd(), ".")
    reqts_txt.write_text(contents_rel_path)


def pelican_run(cmd):
    if os.getenv("DEBUG"):
        cmd = " --debug"

    cmd += " " + program.core.remainder  # allows to pass-through args to pelican
    pelican_main(shlex.split(cmd))
