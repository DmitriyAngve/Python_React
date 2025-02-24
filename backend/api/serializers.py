from django.contrib.auth.models import User
from rest_framework import serializers


# создается сериализатор, который наследуется от serializers.ModelSerializer. Это означает, что он будет автоматически работать с моделью Django (User) и предоставлять удобные методы для сериализации и десериализации данных
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only" : True}}
        #  extra_kwargs = {"password": {"write_only" : True}} - пароль можно передавать в запросах, но он не будет отображаться в ответах

# validate_data - это словарь с данными, которые прощли валидацию
# метод create_user автоматически хеширует пароль перед сохранением пользователя в БД
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user