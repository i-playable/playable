from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^(?P<code>\w+)$', 'product.views.product',
                           name='product_url'),
                       )
