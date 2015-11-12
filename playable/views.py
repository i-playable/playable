from django.http import Http404
from django.shortcuts import render_to_response
from product.models import Product


def home(request):
    response = {
        'uc': Product.objects.filter(category__name='Universal Curriculum'),
        'ar': Product.objects.filter(category__name='Active Reader'),
        'al': Product.objects.filter(category__name='Active Learnser'),
        'articles': range(3),
        'products': Product.objects.filter()[:3],
    }
    return render_to_response('index.html', response)
