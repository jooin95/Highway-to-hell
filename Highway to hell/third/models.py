from django.db import models


# Create your models here. 6번째
class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
## 7번째 콘솔 makemigrations,migrate,shell (DB) -> 모델이 바뀌면 해줌
##from third.models import Restaurant (DB)
## all exclude filter (created_at__gt or lt) startswith endswith range(유사 between)
## paging [] 사용하기 order_by('created_at') 오래된순 -> - 최신순
##shell 종료


class Review(models.Model):
    point = models.IntegerField()
    comment = models.CharField(max_length=500)

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    #레스토랑에 대한 외래키, 레스토랑이 사라졌을 때 삭제하겠다. set null은 삭제되도 삭제 안됨
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
