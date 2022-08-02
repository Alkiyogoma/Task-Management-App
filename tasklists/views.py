from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse

#Loaded Forms
from .forms import *

from .models import *

def index(request):
    data ={} 
    data['tasks'] = Task.objects.all()
    data['users'] = Users.objects.all()
    return render(request , 'pages/index.html', data)

def details(request, task_id):
    task_details = get_object_or_404(Task, pk=task_id) 
    others = Task.objects.all()
    return render(request, 'pages/details.html', {'task': task_details, 'others': others})

def create_view(request): 
    # dictionary for initial data with  
    # field names as keys 
    context ={} 
  
    # add the dictionary during initialization 
    form = TaskTypeForm(request.POST or None) 
    if form.is_valid(): 
        form.save() 

    context['form']= form 
    return render(request, "pages/add_tasktype.html", context) 

        
def show(request):  
    employees = Task.objects.all()  
    return render(request,"show.html",{'employees':employees})  

def edit(request, id):  
    employee = Task.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})  

def update(request, id):  
    employee = TaskType.objects.get(id=id)  
    form = TaskTypeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'employee': employee})

def destroy(request, id):  
    employee = TaskType.objects.get(id=id)  
    employee.delete()  
    return redirect("/show") 

def profile(request, id): 
    user = Users.objects.get(id=id)  
    form = usersForm(request.POST, instance = user) 
    if form.is_valid(): 
        form.save() 

    return render(request, "pages/profile.html",  {'user': user}) 
