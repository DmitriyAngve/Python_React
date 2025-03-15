from django.urls import path
from . import views

# Это маршрутизация URL в Django, где используется urlpatterns, определяющий пути для обработки запросов
# path("notes/", views.NoteListCreate.as_view(), name="note_list"):
# URL: notes/
# Класс-представление: views.NoteListCreate.as_view()
# Название маршрута: "note_list"
# Этот маршрут указывает, что при обращении к notes/ вызывается представление NoteListCreate

#  path("notes/delete/<int:pk>", views.NoteDelete.as_view(), name="delete-note")
# URL: notes/delete/<int:pk> (Например notes/delete/5)
# Класс-представление: views.NoteDelete.as_view()
# Название маршрута: delete-note
# Этот маршрут указывает, что при обращении к notes/delete/5 вызывается представление NoteDelete, которое удаляет заметку ID 5
urlpatterns = [
    path("notes/", views.NoteListCreate.as_view(), name ="note_list"),
    path("notes/delete/<int:pk>", views.NoteDelete.as_view(), name="delete-note")
]