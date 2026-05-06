from django.shortcuts import render, redirect
from .forms import ContactoForm
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def contacto(request):

    if request.POST:
        form = ContactoForm(request.POST)

        if form.is_valid(): 
            form.enviar_email()
            messages.success(request, "Su solicitud fue enviada. Nos pondremos en contacto a la brevedad.")
            return redirect("contacto")
    else:
        form = ContactoForm()

    return render(request, 'core/contacto.html', {
        "form": form
    })