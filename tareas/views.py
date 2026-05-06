from django.shortcuts import render, redirect
from .models import Tarea
from django.contrib.auth.decorators import login_required
from .forms import TareaForm
from django.contrib import messages

# Create your views here.


@login_required
def index(request):
    """
    tareas = Tarea.objects.all()
    respuesta = "<ul>"
    for tarea in tareas:
        respuesta += f"<li>{tarea}</li>"

    respuesta += "</ul>"
    return HttpResponse(respuesta)
    """
    return render(request, "tareas/index.html", {
        "tareas": Tarea.objects.filter(usuario=request.user).order_by("-id")
    })


@login_required
def crear(request):

    if request.POST:
        form = TareaForm(request.POST)

        if form.is_valid():
            """
            tarea = Tarea()
            tarea.titulo = form.cleaned_data.get("titulo")
            tarea.completado = form.cleaned_data.get("completado")
            tarea.save()
            """
            tarea = form.save(commit=False)
            tarea.usuario = request.user
            tarea.save()
            messages.success(request, "Tarea creada correctamente")
            return redirect("tareas:index")
    else:
        form = TareaForm()

    return render(request, "tareas/crear.html", {
        "form": form
    })
