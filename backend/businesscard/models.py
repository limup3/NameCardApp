from os import name
from django.db import models
from django.contrib.auth.models import User
from businesscardbook.models import BusinessCardBook
from businesscardocr.models import BusinessCardOcr

# Create your models here.


class BusinessCard(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="BusinessCard")
    book_id = models.ForeignKey(
        BusinessCardBook,
        on_delete=models.SET_NULL,
        related_name="BusinessCard",
        null=True,
        blank=True,
    )
    ocr_id = models.ForeignKey(
        BusinessCardOcr,
        on_delete=models.CASCADE,
        related_name="BusinessCard",
        null=True,
        blank=True,
    )
    name = models.CharField("이름", max_length=150, blank=True, default="")
    company_name = models.CharField("회사명", max_length=50, blank=True, default="")
    position = models.CharField("직책", max_length=50, blank=True, default="")
    department = models.CharField("부서", max_length=50, blank=True, default="")
    direct = models.CharField("직통번호", max_length=20, blank=True, default="")
    phone = models.CharField("유선전화", max_length=20, blank=True, default="")
    mobile = models.CharField("휴대폰", max_length=20, blank=True, default="")
    fax = models.CharField("팩스", max_length=30, blank=True, default="")
    email = models.CharField("이메일", max_length=250, blank=True, default="")
    address = models.TextField("주소", blank=True, default="")
    eng_name = models.CharField("영문 이름", max_length=150, blank=True, default="")
    eng_company_name = models.CharField("영문 회사명", max_length=100, blank=True, default="")
    eng_position = models.CharField("영문 직책", max_length=100, blank=True, default="")
    eng_deptment = models.CharField("영문 부서", max_length=50, blank=True, default="")
    eng_address = models.TextField("영문 주소", blank=True, default="")
    my_bc = models.BooleanField("본인명함 여부")
    inquiry_date = models.DateTimeField("마지막 조회일", blank=True, null=True)
    create_date = models.DateTimeField("등록일", auto_now_add=True)
    update_date = models.DateTimeField("마지막 수정일", auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "명함"
        verbose_name_plural = "명함 목록"
        ordering = ["-create_date"]
