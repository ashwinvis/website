---
Title: Testing comments on Fediverse
Author: Ashwin Vishnu Mohanan
Date: 2021-12-19T15:30:21.275472
Slug: testing-comments-on-fediverse
Status: published
Summary: A tiny javascript to backfeed replies
Category: Tech Talk
Tags: software
FediID: 107474616123937050
---

Thanks to:

- <https://carlschwan.eu/2020/12/29/adding-comments-to-your-static-blog-with-mastodon/>
- <https://blog.xmgz.eu/jekyll-mastodon-comment/>
- <https://fossacademic.tech/2021/12/16/CommentsTest.html>

I have found a way to integrate comments from Fediverse into the blog. The
implementation is integrated into my Pelican theme. See 
[this
commit](https://codeberg.org/ashwinvis/m.css/commit/d5093d090f3e8458e53f5f4b534f757ffb311d57).
Now, I need to find a smart way to automate this workflow -- possibly using the
command line Toot client.
