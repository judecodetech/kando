from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from api import urls as api_urls

urlpatterns = [
    url(r'', include('frontend.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(api_urls, namespace='api')),
] + staticfiles_urlpatterns()
