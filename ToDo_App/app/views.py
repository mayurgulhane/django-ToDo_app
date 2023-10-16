from django.shortcuts import render,HttpResponse,redirect
from .models import Task
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as loginAuth,logout as logoutAuth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

# Login 
def login(request):
    if request.method == "POST":
        userName = request.POST['username']
        password = request.POST['password']
        user = authenticate( username=userName, password=password)
        if user is None:
            messages.error(request, "Invalid username or password")
            return redirect('login')
        else:
            loginAuth(request,user)
            messages.success(request, "You have successfully signed in")
            return redirect('Home')
    return render(request,'login.html')


# Register
def register(request):
    if request.method == "POST":
        fullName=request.POST.get('name')
        userName=request.POST.get('user')
        email=request.POST.get('email')
        password=request.POST.get('password')

        user = User.objects.filter(username=userName)
        if user.exists():
            messages.error(request, "Username already taken.")
            return redirect('register')

        user=User.objects.create(
            first_name = fullName,
            username = userName,
            email = email
            )
        user.set_password(password)
        user.save()

        messages.success(request, "Registration completed successfully")
        return redirect('login')
    return render(request,'register.html')


# logout
def logout(request):
    logoutAuth(request)
    return redirect('login')


# Home page
@login_required
def index(request):
    inCompletedTasks = Task.objects.filter(user=request.user,is_completed=False).order_by('-updated_at')
    completedTasks = Task.objects.filter(user=request.user,is_completed=True)

    context={
        'inCompletedTasks' : inCompletedTasks,
        'completedTasks' : completedTasks,
    }
    return render(request,'index.html', context)


# Create task
@login_required
def createTask(request):
    if request.method == "POST":
        task = request.POST['task']
        addTask=Task(user=request.user,task=task)
        addTask.save()

    messages.success(request, "Successfully added task")
    return redirect('Home')


# Complete task
@login_required
def completed(request,pk):
    completedTasks = Task.objects.get(pk=pk)  # get the task
    completedTasks.is_completed=True 
    completedTasks.save()
    return redirect('Home')


# Incomplete task
@login_required
def inComplete(request,pk):
    inCompleteTask = Task.objects.get(pk=pk) # get the task
    inCompleteTask.is_completed=False
    inCompleteTask.save()
    return redirect('Home')


# Update task
@login_required
def updateTask(request,id):
    task = Task.objects.get(id=id)
    if request.method == "POST":
        updateTask = request.POST['updateTask']
        task.task=updateTask
        task.save()
        messages.success(request, "Updated Task")
        return redirect('Home')
    
    context={
        'task':task
    }
    return render(request,'update.html',context)


# Delete task
@login_required
def deleteTask(request,id):
    task = Task.objects.get(id=id)
    task.delete()
    messages.success(request, "Deleted Task")
    return redirect('Home')