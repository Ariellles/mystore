from django import forms
from .models import Purchase, Profile
from django.contrib.auth.forms import UserCreationForm


class ContactForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    birth_day = forms.DateField(widget=forms.SelectDateWidget, required=False, label='Date of Birth')
    message = forms.CharField(max_length=500, widget=forms.Textarea)


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = '__all__'
        widgets = {
            'product': forms.HiddenInput()
        }


class RegisterUserForm(UserCreationForm):

    def save(self):
        new_user = super().save()
        new_profile = Profile.objects.create(user=new_user)
        return new_user
