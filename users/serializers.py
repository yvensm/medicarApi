from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)
        extra_kwargs = {
            'passwrod': {'write_only': True}
        }

    def validate(self, data):
        def validate_email(data):
            try:
                user = User.objects.get(email=data['email'])
                raise serializers.ValidationError(
                    {'email': 'Um usuário com este email já existe.'})
            except User.DoesNotExist:
                pass

        validate_email(data)
        return data

    def save(self,):
        user = User(
            username=self.validated_data['username'], email=self.validated_data['email'])
        user.set_password(self.validated_data['password'])
        user.save()
        return user
