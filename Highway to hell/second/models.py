from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)    #데이터가 게시글 데이터가 실행될때 현재시간
    updated_at = models.DateTimeField(auto_now=True)        #생성될 떄 x 수정할때 바뀌는 값

    # num_stars = models.IntegerField() 숫자 필드생성