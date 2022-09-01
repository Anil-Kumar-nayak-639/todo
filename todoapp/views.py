from ast import Return
from django.shortcuts import render,redirect
from todoapp.models import todolist
from todoapp.forms import TodoForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    return render(request,"index.html")

def contact(request):
    return render(request,"contact.html")

def about(request):
    return render(request,"about.html")



@login_required
def todo_list(request):
    if request.method=="POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.manage = request.user
            instance.save()
            messages.success(request,("Task Added"))
            return redirect ("todo_list")
    else:    
        obj=todolist.objects.filter(manage=request.user)
        paginator=Paginator(obj,5)
        page=request.GET.get('pg')
        obj=paginator.get_page(page)
        return render(request,"todo_list.html",{'obj':obj})


@login_required
def delete_list(request,id):
    obj=todolist.objects.get(pk=id)
    if obj.manage == request.user:
        obj.delete()
    else:
        messages.error(request,("Action Restricted"))
    messages.success(request,("Task Deleted"))
    return redirect("todo_list")


@login_required
def update_list(request,id):
    if request.method=="POST":
        obj=todolist.objects.get(pk=id)
        form=TodoForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()        
            messages.success(request,("Task Updated."))
            return redirect ("todo_list")
    else:    
        list_obj=todolist.objects.get(pk=id)
        return render(request,"update.html",{'list_obj':list_obj})

def complete_list(request,id):
    obj=todolist.objects.get(pk=id)
    if obj.manage == request.user:
        obj.done=True
        obj.save()
    else:
        messages.error(request,("Action Restricted"))
    return redirect("todo_list")

def pending_list(request,id):
    obj=todolist.objects.get(pk=id)
    if obj.manage == request.user:
        obj.done=False
        obj.save()
    else:
        messages.error(request,("Action Restricted"))
    return redirect("todo_list")