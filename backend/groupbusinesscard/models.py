from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class GroupBusinessCard(models.Model):
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='groupbusinesscard')
    name = models.CharField("그룹 이름", max_length=30)
    create_date = models.DateTimeField("등록일", auto_now_add=True)
    update_date = models.DateTimeField("마지막 수정일", auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '그룹 명함첩'
        verbose_name_plural = '그룹 명함첩 목록'
        ordering = ['-create_date']
