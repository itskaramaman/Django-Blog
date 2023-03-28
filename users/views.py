from django.shortcuts import render, redirect
from .forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def register(request):
    
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        import ipdb;ipdb.set_trace()
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! You are now able to Login')
            return redirect('users-login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})

@login_required
def profile(request, id=None):
    profile_user = request.user
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, 
                                    request.FILES, 
                                    instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('users-profile')
    else:
        if id:
            profile_user = User.objects.get(id=id)
            u_form = UserUpdateForm(instance=profile_user)
            p_form = ProfileUpdateForm(instance=profile_user.profile)
        else:
            u_form = UserUpdateForm(instance=request.user)
            p_form = ProfileUpdateForm(instance=request.user.profile)


    context = {
        'profile_user': profile_user,
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)





