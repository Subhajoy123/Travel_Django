from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'home.html', {'name':'Addition'})


def add(request):
    v=int(request.POST['num1'])
    w=int(request.POST['num2'])
    res=v+w
    return render(request, 'result.html', {'result':res})