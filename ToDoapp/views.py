from django.shortcuts import render,redirect
from django.views.generic import View
from ToDoapp.models import Todo
from django import forms


# Create your views here.

class TodoListView(View):
    def get(self, request, *args, **kwargs):
        qs=Todo.objects.all()
        return render(request,'todo_list.html',{'qs':qs})
    
class TodoForm(forms.ModelForm):
    class Meta:
        model=Todo
        fields='__all__'
        
class TodoCreateView(View):
    def get(self, request, *args, **kwargs):
        form = TodoForm()
        return render(request,'todo_create.html',{'form':form})
    def post(self, request, *args, **kwargs):
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo-list')
        else:
            return render(request,'todo_create.html',{'form':form})
        
# todo detail view
# localhost:8000/todo/id/
# method get

class TodoDetailView(View):
    def get(self, request,*args,**kwargs):
        id=kwargs.get('pk')
        qs=Todo.objects.get(id=id)
        return render(request,'Todo_details.html',{'data':qs})
            
            
class TodoDeleteView(View):
    def get(self, request, *args, **kwargs):
        id=kwargs.get('pk')
        Todo.objects.get(id=id).delete()
        return redirect('todo-list')
    
class TodoUpdateView(View):
    def get(self, request, *args, **kwargs):
        id=kwargs.get('pk')
        todo_object=Todo.objects.get(id=id)
        form=TodoForm(instance=todo_object)
        return render(request,'todo_edit.html',{'form':form})
    
    
    def post(self, request,args,*kwargs):
        id=kwargs.get('pk')
        todo_object=Todo.objects.get(id=id)
        form=TodoForm(request.POST,instance=todo_object)
        if form.is_valid():
            form.save()
            return redirect('todo-list')
        else:
            return render(request, 'todo_list.html',{'form':form})