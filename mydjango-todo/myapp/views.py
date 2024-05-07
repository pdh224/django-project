from django.shortcuts import render, get_object_or_404 #템플릿 문서 전달하기
from django.http import HttpResponse
from myapp.models import Todo
from .forms import TodoForm
from django.shortcuts import redirect
from datetime import datetime
# Create your views here.
#context:템플릿 문서에 표시할 정보르 전달하는 매개변수
def index(request):
    
    Todo_qs=Todo.objects.all()

    return render(
        request=request,
        template_name="myapp/index.html",
        context={
            "Todo_qs": Todo_qs
        }
    )
def todo_create(request):
    if request.method == 'POST':
        todo = Todo(
            day=datetime.now(),
            todo=request.POST.get("todo")
        )
        todo.save()
        
        return redirect('index')
    else:
        form = TodoForm()
        context = {'form': form}
        return render(request, 'myapp/todo_form.html', context)

def delete_todo(request, todo_id):
    if request.method=="POST":
        todo=get_object_or_404(Todo, id=todo_id)
        todo.delete()
    return redirect('index')