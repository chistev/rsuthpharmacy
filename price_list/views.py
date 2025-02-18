from django.core.paginator import Paginator
from django.shortcuts import render
from price_list.models import Category, Product

def index(request):
    categories = Category.objects.all()
    selected_category_slug = request.GET.get('category', None)

    if selected_category_slug:
        category = Category.objects.get(slug=selected_category_slug)
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()

    # Pagination: Show 8 products per page
    paginator = Paginator(products, 40)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'price_list/index.html', {
        'categories': categories,
        'page_obj': page_obj
    })
