from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import settings



urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\
+ staticfiles_urlpatterns()