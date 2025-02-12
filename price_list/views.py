from django.shortcuts import render

from price_list.models import Category


def index(request):
    categories = Category.objects.all()
    return render(request, 'price_list/index.html',
                  {'categories': categories})
