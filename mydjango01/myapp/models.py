from django.db import models
"""
모델을 추가했다는 것은 사용할 데이터 유형을 추가했다는 것이다.
따라서 db 파일에 테이블도 같이 추가해주어야 모든 것이 정상 동작한다.
내가 직접 정의한 모델을 테이블에 추가하려면 두단계에 걸쳐 마이그레이션 작업을 해주어야 한다
1.마이그레이션 내용 정리하기:makemigrations
2.실제로 테이블에 반영하기:migrate
"""
# Create your models here.
class Item(models.Model):
    name=models.CharField(max_length=30)
    note=models.TextField()