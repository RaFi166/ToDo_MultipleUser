from django.shortcuts import render,redirect
from django.http import HttpResponse
from task.models import Task
from task import forms
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

#home:
@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        user = request.user

        form = forms.Taskform()
        all_data = Task.objects.filter(user = user).order_by('priority')
        context = {'form': form , 'all_data': all_data}
        return render(request,'home.html',context=context)


#signup:
def signup(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:         
            user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
            user.save()
            return redirect('home')
        else:
            print("password dont match")
    else:
        return render(request, 'signup.html' )

#login:
def login (request):
    if request.method== "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            print("user is login")
            return redirect('home')     
        else:
            return redirect ('login')
    else:
        return render (request, 'login.html')

#logout:
def logout (request):
    auth.logout(request)
    return redirect ('signup')

@login_required(login_url='login')
def task_save(request):
    if request.user.is_authenticated:
        user = request.user
        print(user)
        form =  forms.Taskform(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            print(todo)
            return redirect("home")
        else: 
            return render(request , 'index.html' , context={'form' : form})

        
def delete_task(request,id):
    Task.objects.get(pk = id).delete()
    return redirect('home')


def change_task(request, id, status):
    tasks = Task.objects.get(pk = id)
    
    tasks.status = status
    tasks.save()
    return redirect ("home") 
