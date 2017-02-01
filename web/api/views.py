from django.contrib.auth import get_user_model, update_session_auth_hash

from rest_framework import status, views
from rest_framework.response import Response

from api import serializers


class UserPasswordView(views.APIView):
    serializer_class = serializers.UserPasswordSerializer
    queryset = get_user_model().objects.all()

    def get_queryset(self):
        """
        Only return the currently logged in user.
        """
        user = self.request.user
        return self.queryset.filter(id=user.id)

    def post(self, request, *args, **kwargs):
        """
        Change your password.
        """
        user = request.user

        serializer = self.serializer_class(
            data=request.data, context={'request': request, 'user': user, })

        if serializer.is_valid():
            user.set_password(serializer.data['new_password'])
            user.save(force_update=True)
            update_session_auth_hash(request, user)
            return Response({'detail': 'Password successfully changed.'})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
