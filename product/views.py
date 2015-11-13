from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from product.models import Product


def product(request, code):
    product = get_object_or_404(Product, code=code)
    return render_to_response('product.html', {
                              'product': product,
                              }, context_instance=RequestContext(request))
