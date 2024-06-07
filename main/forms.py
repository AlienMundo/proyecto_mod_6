from django import forms

class ContactForm(forms.Form):
  nombre = forms.CharField(
    max_length=64,
    widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nombre'}))
  email = forms.EmailField(
    max_length=15, 
    label='Correo Electrónico', 
    widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Correo Electrónico'})
    )
  edad = forms.IntegerField(
    required=False,
    widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Edad'}),

  )
