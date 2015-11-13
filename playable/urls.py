from django.conf.urls import include, url, patterns


from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django_markdown import flatpages


import settings

admin.autodiscover()
flatpages.register()

urlpatterns = [
    url(r'^$', 'playable.views.home', name='homepage_urls'),
    url(r'^product/', include('product.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url('^markdown/', include('django_markdown.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\
    + staticfiles_urlpatterns()

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)),
                            )
