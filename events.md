---
layout: page
title: 'Events'
---

<div class="list-filters">
  <a href="/posts" class="list-filter">News</a>
  <a href="/events" class="list-filter filter-selected">Events</a>
  <a href="/tutorials" class="list-filter">Tutorials</a>
  <a href="/tags" class="list-filter">Index</a>
</div>

{% if site.tags contains 'Events' %}
{% assign posts = site.tags['Events'] %}
{% endif %}
<div class="posts-list">
    {% for post in posts %}
    <article>
        <a class="post-preview" href="{{ post.url | prepend: site.baseurl }}">
            <h2 class="post-title">{{ post.title }}</h2>
            {% if post.subtitle %}
            <h3 class="post-subtitle">
            {{ post.subtitle }}
            </h3>
            {% endif %}
        <p class="post-meta">
            Posted on {{ post.date | date: "%B %-d, %Y" }}
        </p>
        <div class="post-entry">
            {{ post.content | truncatewords: 50 | strip_html | xml_escape}}
        </div>
        </a>  
    </article>
    {% endfor %}
</div>
