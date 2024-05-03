from django.shortcuts import render #템플릿 문서 전달하기
from django.http import HttpResponse
from myapp.models import Item


# Create your views here.
#context:템플릿 문서에 표시할 정보르 전달하는 매개변수
def index(request):
    
    item_qs=Item.objects.all()

    return render(
        request=request,
        template_name="myapp/index.html",
        context={
            "item_qs": item_qs
        }
    )

