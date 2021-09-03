from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import UserCreateForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import login
#from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def sign_up(request):
    context={}
    form = UserCreateForm(request.POST or None)
    if(request.method == 'POST'):
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('posts:index')
    context['form'] = form
    return render(request,'accounts/sign_up.html',context)

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance = request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Profile details updated.')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)

    context = {
        'u_form':u_form,
        'p_form':p_form
    }

    return render(request,'accounts/profile.html',context)
