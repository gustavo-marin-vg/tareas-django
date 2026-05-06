from django import forms


class ContactoForm(forms.Form):
    asunto = forms.CharField(
        max_length=200
    )
    nombre = forms.CharField(
        max_length=200
    )
    email = forms.EmailField(
        max_length=300
    )
    mensaje = forms.CharField(
        max_length=2000,
        widget=forms.Textarea()
    )
    acepta = forms.BooleanField()

    def enviar_email(self):
        print(f"""
            Enviando un e-mail.
            Asunto: {self.cleaned_data.get("asunto")}
            Nombre: {self.cleaned_data.get("nombre")}
            E-mail: {self.cleaned_data.get("email")}
            Mensaje: {self.cleaned_data.get("mensaje")}
        """)
