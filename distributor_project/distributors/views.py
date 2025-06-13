# distributors/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import DistributorRegistrationForm
from .models import Distributor

def register_distributor(request):
    if request.method == 'POST':
        # If the form is submitted, process the data
        form = DistributorRegistrationForm(request.POST)
        if form.is_valid():
            form.save() # This saves the data to the Distributor model
            # Redirect to a new URL to show a success message
            return redirect('register_success') # We will create this URL next
    else:
        # If it's a GET request, just show a blank form
        form = DistributorRegistrationForm()

    context = {'form': form}
    return render(request, 'distributors/register.html', context)

def register_success(request):
    return render(request, 'distributors/register_success.html')

def view_profile(request, pk):
    # Get the specific distributor object or show a 404 page if not found
    distributor = get_object_or_404(Distributor, pk=pk)
    context = {'distributor': distributor}
    return render(request, 'distributors/profile_view.html', context)

def update_profile(request, pk):
    distributor = get_object_or_404(Distributor, pk=pk)
    if request.method == 'POST':
        # The 'instance=distributor' part is key. It tells the form
        # that we are UPDATING an existing object, not creating a new one.
        form = DistributorRegistrationForm(request.POST, instance=distributor)
        if form.is_valid():
            form.save()
            return redirect('profile_view', pk=distributor.pk) # Redirect back to the profile view
    else:
        # Pre-fill the form with the distributor's current data
        form = DistributorRegistrationForm(instance=distributor)

    context = {'form': form, 'distributor': distributor}
    return render(request, 'distributors/profile_update.html', context)

def distributor_list(request):
    distributors = Distributor.objects.all().order_by('company_name') # Get all distributors
    context = {'distributors': distributors}
    return render(request, 'distributors/distributor_list.html', context)



