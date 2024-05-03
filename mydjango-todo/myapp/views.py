from django.shortcuts import render #템플릿 문서 전달하기
from django.http import HttpResponse
from myapp.models import Todo
from .forms import TodoForm
from django.shortcuts import redirect
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
        form = TodoForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.save()
            return redirect('index')
    else:
        form = TodoForm()
    context = {'form': form}
    return render(request, 'myapp/todo_form.html', context)