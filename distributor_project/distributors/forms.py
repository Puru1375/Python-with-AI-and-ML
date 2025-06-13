# distributors/forms.py
from django import forms
from .models import Distributor

class DistributorRegistrationForm(forms.ModelForm):
    class Meta:
        model = Distributor
        # We can choose which fields to show in the form
        fields = ['company_name', 'contact_person', 'email', 'phone_number', 'address']

        # Optional: You can add HTML attributes to the form widgets here
        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Company LLC'}),
            'contact_person': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'John Doe'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'you@company.com'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+1-202-555-0149'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }