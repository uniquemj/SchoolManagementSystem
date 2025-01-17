from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from accounts.forms import CustomUserCreationForm
# Create your views here.
User = get_user_model()

def user_login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        try: 
            account = User.objects.get(email = email)
        except User.DoesNotExist:
            messages.error(request, "Account with this Email doesn't exist")
            return redirect('accounts:sign-in')
        password = request.POST.get('password')
        
        if not account.check_password(password):
            messages.error(request, "Login failed: Password incorrect.")

        user = authenticate(email=email, password = password)
        if user != None:
            login(request, user)
            messages.success(request, "User Logged In.")
            return redirect('dashboard:home')
    return render(request, 'accounts/user-login.html')

def user_registration(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "User Registered")
            return redirect('accounts:sign-in')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'accounts/user-register.html', {'form':form})



def user_logout(request):
    logout(request)
    messages.success(request, 'User Logged out!!')
    return redirect('accounts:sign-in')
