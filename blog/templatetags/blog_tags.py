from django import template
from ..models import Post
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown

#creating a custom tag to display total number of published posts
register=template.Library()
@register.simple_tag
def total_posts():
    return Post.published.count()

#creating a custom inclusion tag
@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts=Post.published.order_by('publish')[:count]
    return {'latest_posts':latest_posts}

#template tag that returns a queryset
@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(total_comments = Count('comments')).order_by('-total_comments')[:count]

#creating a custom template filtering tag
@register.filter(name="markdown")
def markdown_format(text):
    return mark_safe(markdown.markdown(text))