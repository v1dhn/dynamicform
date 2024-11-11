from django.shortcuts import render, redirect
from .models import Profile, DynamicField
from .forms import ProfileForm, DynamicFieldForm
from django.contrib.auth.decorators import login_required

#@login_required
def configure_fields(request):
    if request.method == 'POST':
        form = DynamicFieldForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('configure_fields')
    else:
        form = DynamicFieldForm()
    
    fields = DynamicField.objects.all()
    return render(request, 'configure_fields.html', {'form': form, 'fields': fields})

#@login_required
def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile_list')
    else:
        form = ProfileForm()
    return render(request, 'create_profile.html', {'form': form})

#@login_required
def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, 'profile_list.html', {'profiles': profiles})
