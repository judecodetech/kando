from django.conf.urls import url

from rest_framework import routers

from api import views, viewsets


router = routers.DefaultRouter()

router.register(r'actions', viewsets.ActionViewSet)
router.register(r'tags', viewsets.TagViewSet)
router.register(r'tasks', viewsets.TaskViewSet)
router.register(r'team', viewsets.TeamViewSet)
router.register(r'user', viewsets.UserViewSet)

urlpatterns = [
    url(r'change-password', views.UserPasswordView.as_view(), name='change-password'),
] + router.urls
