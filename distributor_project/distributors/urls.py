# distributors/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # The homepage to list all distributors
    path('', views.distributor_list, name='distributor_list'),

    # The page to register a new distributor
    path('register/', views.register_distributor, name='register'),
    
    # 👇 ADD THIS LINE for the registration success page 👇
    path('register/success/', views.register_success, name='register_success'),

    # The pages for viewing and updating a profile
    path('profile/<int:pk>/', views.view_profile, name='profile_view'),
    path('profile/<int:pk>/update/', views.update_profile, name='profile_update'),
]