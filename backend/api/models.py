from django.db import models
from django.contrib.auth.models import User


# Определяю модель Django Note, представляющую заметку.
# title - для хранения заголовка
# content - для хранения текста заметки, не имеет огр. по длине
# created_at - это поле автомат. сохраняет дату и время создания заметки
# author - указывает на связь с моделью User(это поль-ль, создавший заметку). Позволяет получить все заметки пользователя с помощью related_namr="notes"
# on_delete=models.CASCADE - это чтобы при удалении юзером заметки удалялось все по каскаду

# def __str__(self): - определяет строковое представление объекта (для админки django)

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")

    def __str__(self):
        return self.title