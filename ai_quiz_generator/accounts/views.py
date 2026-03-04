from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
def register(request):
    if request.method == "GET":
        return render(request,"accounts\\register.html")
    if request.method == "POST":
        first_name = request.POST.get('f_name')
        last_name = request.POST.get('l_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        conf_password = request.POST.get('conf_password')
        
        if password != conf_password:
            return render(request,"accounts\\register.html",{'error':"Passwords do not match"})

        try:
            existing_user = User.objects.get(email=email)
            return render(request,"accounts\\register.html",{'error':"Already the user exists with this email"})
        except User.DoesNotExist:
            try:
                User.objects.create_user(username=email,email=email,first_name=first_name,last_name=last_name,password=password)
                return render(request,"accounts\\register.html",{'success':"User Registered Successfully"})
            except Exception as e:
                return render(request,"accounts\\register.html",{'error':e})
        
        # return render(request,"accounts\\register.html")
        