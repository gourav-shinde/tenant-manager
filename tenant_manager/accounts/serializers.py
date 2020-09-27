from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
        )
        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=['username', 'email']
            )
        ]

class RegisterationSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={'Input_type':'password'},write_only=True)

    class Meta:
        model = User
        fields = ['email','username','password','password2']
        extra_kwargs={
            'password':{'write_only':True}
        }

    def save(self):
        account=User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )
        password=self.validated_data['password']
        password2=self.validated_data['password2']

        if password!=password2:
            raise serializers.ValidationError({'password':'passwords must match'})

        account.set_password(password)
        account.save()
        return account