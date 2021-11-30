from django.shortcuts import render
from tecnologias.models import comentarios

publicaciones = lambda: tuple(comentarios.objects.all())

def index(request):
    return render(request, 'index.html')

def tecno(request):
    return render(request, 'tecnologias/tecno.html', {"posts": publicaciones()})


def comentar(request):
    response = "Error, vuelva a intentarlo"
    if request.method == 'POST':
        user = request.POST['user']
        text = request.POST['text']

        if user and text:
            try:
                comentarios.objects.create(usuario=user, comentario=text)
                response = "Comentario publicado"
            except:
                response = "Error, comentario no publicado"
        else: response = "Error, Datos vacios"
    return render(request, 'tecnologias/tecno.html', {"response": response, "posts": publicaciones()})

def about(request):
    return render(request, 'about.html')