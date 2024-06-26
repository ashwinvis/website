# Ashwin's [fluid.quest](https://fluid.quest) website

[![Build Status](https://github.com/ashwinvis/ashwinvis.github.io/workflows/Publish%20pelican%20website/badge.svg)][actions]

## Requirements

- Python: 3.x, Pelican and other packages (see `requirements.txt`)

## Simple installation

```sh
git clone --recursive https://codeberg.org/ashwinvis/website.git
## or a simple clone followed by
# git submodule update --init --recursive

cd website
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

make html serve
```

## Development

Update `requirements.txt` and launch development server

```sh
pip install -U pip-tools
invoke -e pip-compile && pip-sync

invoke livereload
```

**Tip**: To conveniently work with submodules:

```sh
git config submodule.recurse true
```

**Optional**: Set up remote repositories for manual deployment

```
git remote add deploy git@codeberg.org:ashwinvis/pages.git

make deploy

```

<!-- TODO: replace github pages with codeberg pages -->

## Write content

Add the following script to `~/.profile`:

```sh
alias blog="/path/to/venv/bin/python -m pelican_ashwinvis.util.write"
```

which is a script encourage writing. [See here for more
details](https://fluid.quest/pelican-mini-cms.html).

## License

This repository contains copyrighted source code from a variety of sources.  In
each instance, the copyright holder has released that source code under some
kind of license.

- All text and media under `content` is distributed under a CC-BY license a
  copy of which is included in the file called `content/LICENSE`.

- `pelican`'s source code and the configuration files for `pelican` is distributed
  under the terms of the GNU Affero General Public License, a copy of which is
  included in the file called `LICENSE`.

- `m.css` is distributed under an MIT license, a copy of which is included in the
  file called `m.css/COPYING`.

- The PWA is distributed under an MIT license, a copy of which is included in
  the file called `content/extra/LICENSE`.

You should read the corresponding license carefully, as it defines your
specific rights regarding the use of covered source code, as well as the
conditions under which those rights are given to you.

[actions]: https://github.com/ashwinvis/ashwinvis.github.io/actions
