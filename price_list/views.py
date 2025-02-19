from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from price_list.models import Category, Product

def index(request, category_slug=None):
    categories = list(Category.objects.all())

    # Move "Others" category to the end
    others_category = next((c for c in categories if c.name.lower() == "others"), None)
    if others_category:
        categories.remove(others_category)
        categories.append(others_category)

    selected_category_slug = category_slug or request.GET.get('category', None)

    # Fetch the selected category or default to "Tablets/Capsules" category
    selected_category = None
    if selected_category_slug:
        selected_category = get_object_or_404(Category, slug=selected_category_slug)
        products = Product.objects.filter(category=selected_category).order_by("brand_name", "generic_name")
    else:
        # If no category is selected, show all products
        products = Product.objects.all().order_by("brand_name", "generic_name")

    # Pagination: Show 40 products per page
    paginator = Paginator(products, 40)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'price_list/index.html', {
        'categories': categories,
        'page_obj': page_obj,
        'selected_category': selected_category,
    })
