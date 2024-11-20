from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage

from .models import Post


def post_list(request):

    posts = Post.objects.all()

    items_per_page = request.GET.get('items', 5)

    paginator = Paginator(posts, items_per_page)

    page_number = request.GET.get('page', 1)

    try:
        page_posts = paginator.get_page(page_number)

    except EmptyPage:
        page_posts = paginator.page(paginator.num_pages)

    return render(request, 'posts/post_page.html', {'page_posts': page_posts})

