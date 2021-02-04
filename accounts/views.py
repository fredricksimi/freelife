from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages


from .forms import UserRegistrationForm
 
# Create your views here.
def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            
            login(request, user)
            redirect_url = request.GET.get('next', 'mainapp:home')
            return redirect(redirect_url)
        else:
            messages.error(request, 'Bad username or password')
    return render(request, 'accounts/login.html', {})

def logout_user(request):
    logout(request)
    return redirect('accounts:login')

# def user_registration(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             email = form.cleaned_data['email']
#             password1 = form.cleaned_data['password1']
#             user = User.objects.create_user(username,email=email, password=password1)
#             messages.success(request, 'Thanks for registering {}' .format(user.username))
#             return redirect('accounts:login')
#             print('form was valid')
#     else: 
#         form = UserRegistrationForm()
 
#     return render(request, 'accounts/register.html', {'form':form})