# distributors/models.py
from django.db import models

class Distributor(models.Model):
    company_name = models.CharField(max_length=200)
    contact_person = models.CharField(max_length=100)
    email = models.EmailField(unique=True) # unique=True ensures no two distributors have the same email
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    registration_date = models.DateTimeField(auto_now_add=True) # Automatically sets the date when created
    is_active = models.BooleanField(default=True)

    def __str__(self):
        # This is how the object will be displayed in the admin panel
        return self.company_name