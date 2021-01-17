from django.db import models
from django.conf import settings

# Create models / 2020-10-15 robert
# imagefield : Pillow 라이브러리 추가 / 2020-10-15 robert


class Notice(models.Model):
    title = models.CharField("제목", max_length=255)
    content = models.TextField("내용")
    image = models.ImageField("이미지",                     
                              upload_to='Notice/%Y/%m/%d', null=True, blank=True)
    create_date = models.DateTimeField("등록일", auto_now_add=True)
    update_date = models.DateTimeField("마지막 수정일", auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '공지사항'
        verbose_name_plural = '공지사항 목록'
        ordering = ['-create_date']

    def get_image_url(self):
        return '%s%s' % (settings.MEDIA_URL, self.image)
