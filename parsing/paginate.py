from django.core.paginator import Paginator, EmptyPage


def paginate(request, posts):
    try:
        page_size = int(request.GET.get("page_size", 3))
    except ValueError:
        page_size = 3
    try:
        page = int(request.GET.get("page", 1))
    except ValueError:
        # Если страница не является целым числом, поставим первую страницу
        page = 1
    paginator = Paginator(posts, page_size)
    try:
        posts = paginator.page(page)
    except EmptyPage:
        # Если страница больше максимальной, доставить последнюю страницу результатов
        posts = paginator.page(paginator.num_pages)

    return posts
