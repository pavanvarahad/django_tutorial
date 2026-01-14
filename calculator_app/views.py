from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def calculator_view(request):
    if request.method == "POST":
        print("POST request received")
        num1 = request.POST.get("num1")
        num2 = request.POST.get("num2")
        if num1 and num2:
            result = int(num1) + int(num2)
        return render(request, "sample.html",{"answer": result})
    elif request.method == "GET":
        print("GET request received")
        return render(request, "sample.html")
