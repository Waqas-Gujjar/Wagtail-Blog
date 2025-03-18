from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase
from taggit.managers import TaggableManager
from modelcluster.tags import ClusterTaggableManager
from datetime import date

class BlogPage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels +[
        FieldPanel('body'),
    ]

    template = "a_blog/blog_page.html"


    def get_context(self, request):
        tag = request.GET.get('tags')
        if tag:
            articles = ArticlePage.objects.filter(tags__name=tag)
        else:
           articles = self.get_children().live().order_by('-first_published_at')
        context = super().get_context(request)
        context['articles'] = articles
        context['tag'] = tag
        return context

class ArticlePage(Page):
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    date = models.DateField("Post date",default=date.today)
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, related_name='+', null=True
    )
    tags = ClusterTaggableManager(through="ArticleTag", blank=True) 
    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('body'),
        FieldPanel('date'),
        FieldPanel('image'),
        FieldPanel('tags'),

    ]

class ArticleTag(TaggedItemBase):
    content_object = ParentalKey(   ArticlePage,on_delete=models.CASCADE, related_name='tagged_items')


