from django import forms

from english.models import MyUser


class ContactForm(forms.Form):
    CHOICES = MyUser.objects.all().values_list("email", "username")
    email = forms.EmailField(widget=forms.Select(attrs={'class': 'form-control'}, choices=CHOICES))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
