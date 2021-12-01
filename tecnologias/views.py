from django.shortcuts import render, redirect
from tecnologias.models import comentarios
from django.contrib import messages

publicaciones = lambda: tuple(comentarios.objects.all())

def index(request):
    return render(request, 'index.html')

def tecno(request):
    return render(request, 'tecnologias/tecno.html', {"posts": publicaciones()})


def comentar(request):
    if request.method == 'POST':
        user = request.POST['user']
        text = request.POST['text']

        if user and text:
            try:
                comentarios.objects.create(usuario=user, comentario=text)
                messages.success(request, "Comentario publicado")
            except:
                messages.success(request, "Error, comentario no publicado")
        else: messages.success(request, "Error, Datos vacios")
    return redirect("tecno")

def about(request):
    return render(request, 'about.html')