from django.shortcuts import render
from .models import *

# Create your views here.
def articles_search(request):
    search_query  = request.GET.get('query', '')
    articles = ArticlePage.objects.live().search(search_query)
    context = {
        'search_query': search_query,
        'articles': articles,
    }
    return render(request, 'a_blog/blog_page.html', context)
   