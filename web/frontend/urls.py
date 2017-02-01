from django.conf.urls import url

from frontend import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^doing/$', views.doing, name='doing'),
    url(r'^review/$', views.review, name='review'),
    url(r'^done/$', views.done, name='done'),
]
