# from django.shortcuts import render,HttpResponse
# from app.models import Task

# def index(request):
#     inCompletedTasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
#     completedTasks = Task.objects.filter(is_completed=True)
#     context={
#         'inCompletedTasks' : inCompletedTasks,
#         'completedTasks' : completedTasks,
#     }
#     return render(request,'index.html',context)





