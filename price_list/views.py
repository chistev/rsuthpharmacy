from django.core.paginator import Paginator
from django.shortcuts import render
from price_list.models import Category, Product

def index(request):
    categories = list(Category.objects.all().order_by("name"))

    # Move "Others" category to the end
    others_category = next((c for c in categories if c.name.lower() == "others"), None)
    if others_category:
        categories.remove(others_category)
        categories.append(others_category)

    selected_category_slug = request.GET.get('category', None)

    if selected_category_slug:
        category = Category.objects.get(slug=selected_category_slug)
        products = Product.objects.filter(category=category).order_by("brand_name", "generic_name")
    else:
        products = Product.objects.all().order_by("brand_name", "generic_name")

    # Pagination: Show 40 products per page
    paginator = Paginator(products, 40)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'price_list/index.html', {
        'categories': categories,
        'page_obj': page_obj
    })
