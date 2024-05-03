from django import forms
from myapp.models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo # 사용할 모델
        fields = ['name', 'todo']