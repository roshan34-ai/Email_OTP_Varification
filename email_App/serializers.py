from rest_framework import serializers
# from email_App.emails import send_otp_via_mail
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'is_varified', 'password']

    def create(self, validated_data):
        user = CustomUser(
                            email=validated_data['email'],
                         )
        user.set_password(validated_data['password'])
        user.save()
        # send_otp_via_mail(validated_data['email'])
        return user


class varifyAccountSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField()