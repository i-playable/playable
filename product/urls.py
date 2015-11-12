from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url('^(?P<slug>[-\w]+)/$', 'product.views.product',
                           name='product_url'),
                       )
