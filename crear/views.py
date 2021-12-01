from django.shortcuts import render, redirect
from crear.models import usuarios
from django.contrib import messages

registros = lambda: usuarios.objects.all()
tarea = lambda id: usuarios.objects.get(id=id)

def insert_read(request):
    if request.method == 'POST':
        titulo = request.POST['title']
        description = request.POST['description']
        if titulo and description:        
            try:
                usuarios.objects.create(titulo=titulo, descripcion=description)
                messages.success(request, "Registro insertado con exito")
            except: 
                messages.success(request, "Error, Tarea no registrada")
        else: messages.success(request, "Error, Datos vacios")
        return redirect("crear:read_insert")
    return render(request, 'crear/crud.html', {"registros": registros()})

def edit(request, id):
    try:
        task = tarea(id)
        return render(request, 'crear/crud.html', {"task": task, "registros": registros()})
    except:
        return render(request, 'crear/404.html', {"id": id})

def update(request, id):
    task = tarea(id)
    if request.method == 'POST':
            task.titulo = request.POST['title']
            task.descripcion = request.POST['description']
            task.save()
            messages.success(request, "Tarea actualizada con exito")
    return redirect("crear:read_insert")

def deleted(request, id):
    task = tarea(id)
    task.delete()
    messages.success(request, "Tarea eliminada con exito")
    return redirect("crear:read_insert")
