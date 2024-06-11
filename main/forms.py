from django import forms

class ContactForm(forms.Form):
  customer_name = forms.CharField(
    max_length=64,
    label = 'Nombre',
    widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nombre'}))
  customer_email = forms.EmailField(
    max_length=40, 
    label='Correo Electrónico', 
    widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Correo Electrónico'})
    )
  message = forms.CharField(
    label = 'Mensaje',
    widget=forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Mensaje'}),

  )
