from rest_framework import serializers

from core import models


class ActionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Action


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Tag


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Task


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.KandoUser


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'email',
            'first_name',
            'last_name',
            'profile_pic'
        )

        extra_kwargs = {
            'email': {'help_text': 'The user\'s email address'},
            'first_name': {'help_text': 'The user\'s first name'},
            'last_name': {'help_text': 'The user\'s last name'},
            'profile_pic': {'help_text': 'An image of the user'},
        }

        model = models.KandoUser


class UserPasswordSerializer(serializers.Serializer):
    current_password = serializers.CharField(help_text='Your current password')
    new_password = serializers.CharField(help_text='Your new password')

    def validate_current_password(self, value):
        user = self.context['user']

        if not user.check_password(value):
            raise serializers.ValidationError('Incorrect password.')

        return value
