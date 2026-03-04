from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from .models import UserProfile
# Create your views here.
def login(request):
    if request.method == "GET":
        return render(request,"accounts\\login.html")
    if request.method == "POST":
        # Handle POST request for form submission
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Perform validation and login logic here
        # For example, check if the user exists, validate password, etc.
        user = authenticate(request, username=email, password=password)

        if user is not None:
            auth_login(request, user)
            return render(request, "accounts/login.html", {"success": "Logged in successfully."})
        else:
            return render(request, "accounts/login.html", {"error": "Invalid email or password"})

def register(request):
    if request.method == "GET":
        return render(request,"accounts\\register.html")
    if request.method == "POST":
        # Handle POST request for form submission
        f_name = request.POST.get("f_name")
        l_name = request.POST.get("l_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        conf_password = request.POST.get("conf_password")

        # Perform validation and registration logic here
        # For example, check if passwords match, validate email, etc.
        if password != conf_password:
            # Handle password mismatch case
            return render(request, "accounts\\register.html", {"error": "Passwords do not match."})
        
        try:
            User.objects.get(username=email)
            return render(request, "accounts\\register.html", {"error": "Email is already registered."})
        except User.DoesNotExist:
            user = User.objects.create_user(username=email, email=email, password=password)
            UserProfile.objects.create(user=user, first_name=f_name, last_name=l_name)
            return render(request, "accounts\\register.html", {"success": "Account created successfully."})

