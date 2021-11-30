from django.shortcuts import render
from crear.models import usuarios

registros = lambda: usuarios.objects.all()
tarea = lambda id: usuarios.objects.get(id=id)

def insert_read(request):
    if request.method == 'POST':
        titulo = request.POST['title']
        description = request.POST['description']
        response = "Error, Vuelva a intentarlo"
        if titulo and description:        
            try:
                usuarios.objects.create(titulo=titulo, descripcion=description)
                response =  "Registro insertado con exito"
            except: 
                response = "Error, Tarea no registrada"
        return render(request, 'crear/crud.html', {"response": response, "registros": registros()})
    return render(request, 'crear/crud.html', {"registros": registros()})

def edit(request, id):
    try:
        task = tarea(id)
        return render(request, 'crear/crud.html', {"task": task, "registros": registros()})
    except:
        return render(request, 'crear/404.html', {"id": id})

def update(request, id):
    task = tarea(id)
    response = "Tarea actualizada con exito"
    if request.method == 'POST':
            task.titulo = request.POST['title']
            task.descripcion = request.POST['description']
            task.save()
    return render(request, 'crear/crud.html', {"registros": registros(), "response": response})

def deleted(request, id):
    task = tarea(id)
    task.delete()
    registros = usuarios.objects.all()
    response = "Tarea eliminada con exito"
    return render(request, 'crear/crud.html', {"response": response, "registros": registros})
