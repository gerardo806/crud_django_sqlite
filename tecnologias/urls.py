from django.urls import path
from tecnologias.views import tecno, comentar, index, about

urlpatterns = [
    path('', index, name="home"),
    path('tecno/', tecno, name="tecno"),
    path('comentar/', comentar, name="comentar"),
    path('about/', about, name="about"),
]