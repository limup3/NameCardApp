from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.


def user_path(instance, filename):
    return "user_{0}/{1}".format(instance.user_id.id, filename)


class BusinessCardOcr(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="businesscardocr")
    image = models.ImageField("이미지", upload_to=user_path, null=True, blank=True)
    OCR_TYPE = (
        ("Recognizing", "인식중"),
        ("Unrecognizable", "인식불가"),
        ("Success", "인식성공"),
    )
    type = models.CharField(
        max_length=50, choices=OCR_TYPE, default="0", help_text="인식 유형", verbose_name="인식 유형"
    )
    create_date = models.DateTimeField("등록일", auto_now_add=True)
    update_date = models.DateTimeField("마지막 수정일", auto_now=True)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = "명함 인식"
        verbose_name_plural = "명함 인식 목록"
        ordering = ["-create_date"]

    def get_image_url(self):
        return "%s%s" % (settings.MEDIA_URL, self.image)
