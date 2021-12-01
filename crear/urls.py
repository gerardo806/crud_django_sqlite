from django.urls import path
from crear.views import deleted, insert_read, edit, update

app_name = "crear"

urlpatterns = [
    path('crud/', insert_read, name="read_insert"),
    path('crud/<int:id>', edit, name="edit"),
    path('deleted/<int:id>', deleted, name="deleted"),
    path('update/<int:id>', update, name="update"),
]