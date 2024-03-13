# aggregator/views.py
import feedparser
from django.http import HttpResponse, JsonResponse
from .models import Article
from django.utils.dateparse import parse_datetime
from dateutil import parser
from django.shortcuts import render
import pprint
from django.shortcuts import render
from django.core import serializers as s


def home(request):
    return HttpResponse("Hello, Django!")

def show_articles(request):
    articles = Article.objects.all().filter(source='Wired').order_by('-publication_date')
    return render(request, 'articles_list.html', {'articles': articles})

def show_articles_json(request):
    articles = Article.objects.all().filter(source='Wired').order_by('-publication_date')
    articles_json = s.serialize('json', articles)
    # return HttpResponse(articles_json, content_type="application/json")
    response = JsonResponse(articles_json, safe=False, content_type="application/json")
    return response

def gather_feed(request):
    feeds = {
        'https://www.wired.com/feed/rss': 'Wired',
        'https://feeds.a.dj.com/rss/RSSWorldNews.xml': 'Wall Street Journal - World News',
    }

    for feed_url, feed_name in feeds.items():
        feed = feedparser.parse(feed_url)

        for entry in feed.entries:
            guid = entry.id
            title = entry.title if 'title' in entry else 'No Title'
            description = entry.summary if 'summary' in entry else 'No Description'
            publication_date = parser.parse(entry.published) if 'published' in entry else None
            author = entry.author if 'author' in entry else 'No Author'
            url = entry.link if 'link' in entry else None

            image_url = 'https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg'
            if 'media_thumbnail' in entry:
                image_url = entry.media_thumbnail[0]['url'] if entry.media_thumbnail else image_url

            # Use update_or_create to either update existing or create new article
            article, created = Article.objects.update_or_create(
                guid=guid,
                defaults={
                    'title': title,
                    'description': description,
                    'publication_date': publication_date,
                    'author': author,
                    'source': feed_name,
                    'url': url,
                    'image_url': image_url,
                }
            )
    # Sort the article chronologically
    articles = Article.objects.all().order_by('-publication_date')

    # Build the HTML content to display articles
    content = '<h1>Articles in Chronological Order</h1>'
    for article in articles:
        content += f"<div><strong>GUID:</strong> {article.guid}<br>"
        content += f"<strong>Publication Date:</strong> {article.publication_date}<br>"
        content += f"<strong>Source:</strong> {article.source}<br>"
        content += f"<strong>Title:</strong> {article.title}<br>"
        content += f"<strong>Author:</strong> {article.author}<br>"
        content += f"<strong>Description:</strong> {article.description}<br>"
        content += f"<strong>URL:</strong> <a href='{article.url}'>{article.url}</a><br>"
        content += f"<strong>Image:</strong> <image src='{article.image_url}' style='max-width:200' alt='alt image'><br>"

        content += f"<strong>Author:</strong> {article.author}<br>"
        content += "</div><br>"

    return HttpResponse(content)
