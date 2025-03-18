from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

class BlogPage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels +[
        FieldPanel('body'),
    ]

    template = "a_blog/blog_page.html"


