from rest_framework import mixins, viewsets

from api import serializers

from core import models
from kandoauth import models as user_model


class AppendOnlyViewSet(
        mixins.CreateModelMixin,
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        viewsets.GenericViewSet):
    """
    A viewset that mimics an append-only log.
    """


class CreateReadUpdateViewSet(
        mixins.CreateModelMixin,
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        viewsets.GenericViewSet):
    """
    A viewset that allows all operations except delete.
    """


class ActionViewSet(AppendOnlyViewSet):
    """
    A vieweset to perform List, Create, and Read on actions
    """
    queryset = models.Action.objects.all()
    serializer_class = serializers.ActionSerializer


class TagViewSet(viewsets.ModelViewSet):
    """
    A vieweset to perform CRUD(Create, Read, Update and Delete)
    on tags
    """
    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """
    A vieweset to perform CRUD(Create, Read, Update, Delete)
    on tasks
    """
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer


class TeamViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = user_model.KandoUser.objects.all()
    serializer_class = serializers.TeamSerializer


class UserViewSet(CreateReadUpdateViewSet):
    """
    A viewset for viewing and creating user instances.
    """
    queryset = user_model.KandoUser.objects.all()
    serializer_class = serializers.UserSerializer

    def get_queryset(self):
        return models.KandoUser.objects.filter(pk=self.request.user.id)
