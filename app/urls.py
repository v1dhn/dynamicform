from django.urls import path
from . import views

urlpatterns = [
    path('configure-fields/', views.configure_fields, name='configure_fields'),
    path('create-profile/', views.create_profile, name='create_profile'),
    path('profile-list/', views.profile_list, name='profile_list'),
]
