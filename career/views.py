from atexit import register
from xml.parsers.expat import model
from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import Student
from django.views import View
# Create your views here.

def index(request):
    dict={}
    return render(request,'career/index.html',context=dict)

def login(request):
    return render(request,'career/login.html')

def contract(request):
    # return render(request,'career/registation.html',)
    if request.method=='GET':
        form=StudentForm()
        return render(request,'career/contract.html', {'form':form})
    else:
        Student=Student.objects.all()
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'career/')

def education(request):
    return render(request,'career/education.html')

def registation(request):
    # if request.method=="POST":
    #     form=StudentForm()
    #     return render(request, 'career/registation.html', {'form':form})
    # else:
    #     form=StudentForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #     return redirect(request,'career/')
    
    form = StudentForm()
    registered = False
    if request.method == 'POST':
        form = StudentForm(data=request.POST)
        if form.is_valid():
            form.save()
            registered = True
            # print("test",form)
    dict = {'form':form,'registered':registered}
    return render(request,'career/registation.html',context=dict)

    
def allstu(request):
    return render(request,'career/allstu.html')

def about(request):
    return render(request,'career/about.html')

def bank(request):
    return render(request,'career/bank.html')

def books(request):
    return render(request,'career/books.html')