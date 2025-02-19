from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from price_list.models import Category, Product

def index(request, category_slug=None):
    categories = list(Category.objects.all())

    # Move "Others" category to the end
    others_category = next((c for c in categories if c.name.lower() == "others"), None)
    if others_category:
        categories.remove(others_category)
        categories.append(others_category)

    selected_category_slug = request.GET.get('category', None) or category_slug
    search_query = request.GET.get('search', '')

    selected_category = None
    products = Product.objects.all().order_by("brand_name", "generic_name")

    if selected_category_slug and selected_category_slug != "all":
        selected_category = get_object_or_404(Category, slug=selected_category_slug)
        products = products.filter(category=selected_category)

    if search_query:
        products = products.filter(
            Q(brand_name__icontains=search_query) |
            Q(generic_name__icontains=search_query)
        )

    paginator = Paginator(products, 40)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'price_list/index.html', {
        'categories': categories,
        'page_obj': page_obj,
        'selected_category': selected_category,
        'search_query': search_query,
    })
