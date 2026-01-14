from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def calculator_view(request):

    num1 = request.GET.get("num1")
    num2 = request.GET.get("num2")
    if num1 and num2:
        result = int(num1) + int(num2)
    else:
        result = "Please provide num1 and num2 as query parameters."
    return render(request, "sample.html",{"answer": result})