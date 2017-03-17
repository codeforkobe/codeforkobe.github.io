---
layout: default
---

# About

ITで神戸をもっと素敵な街にするため活動するコミュニティです。

メインサイトは[Facebook](https://www.facebook.com/codeforkobe)にあります。

* [Code for Kobe Connect](https://www.facebook.com/groups/1536379276600668/) : コミュニティメンバ同士の議論用
* [Slack](https://codeforkobe.slack.com) : チャット
* [イベント参加登録](https://www.codeforamerica.org/brigade/Code-for-Kobe/checkin)
* [イベント活動グラフ](https://www.codeforamerica.org/brigade/Code-for-Kobe/attendance)
* [wiki](https://github.com/codeforkobe/codeforkobe.github.io/wiki)

# Meeting memo

<ul>
{% for post in site.posts %}
<li>
  <a class="post-link" href="{{ post.url }}">{{ post.title }}</a> ---
  <span class="post-meta">{{ post.date | date: "%b %-d, %Y" }}</span>
</li>
{% endfor %}
</ul>

再整理中…

