from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage

from .models import Post


def post_list(request):

    posts = Post.objects.all()

    # Проверяем наличие параметра 'items' в GET-запросе
    items_per_page = request.GET.get('items')

    if items_per_page:
        # Сохраняем значение в сессии, если оно есть
        request.session['items_per_page'] = items_per_page
    else:
        # Используем сохранённое в сессии значение, если оно есть
        items_per_page = request.session.get('items_per_page')

    # Преобразуем в число, если значение найдено, иначе применяем безопасное значение по умолчанию
    items_per_page = int(items_per_page) if items_per_page else 5

    paginator = Paginator(posts, items_per_page)

    page_number = request.GET.get('page', 1)

    try:
        page_posts = paginator.get_page(page_number)

    except EmptyPage:
        page_posts = paginator.page(paginator.num_pages)

    return render(request, 'posts/post_page.html', {'page_posts': page_posts, 'paginator': paginator})

