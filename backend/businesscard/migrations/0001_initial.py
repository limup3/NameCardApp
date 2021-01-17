# Generated by Django 3.1.2 on 2020-11-04 23:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('businesscardbook', '0001_initial'),
        ('businesscardocr', '0002_auto_20201015_1338'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='이름')),
                ('company_name', models.CharField(blank=True, default='', max_length=50, verbose_name='회사명')),
                ('position', models.CharField(blank=True, default='', max_length=50, verbose_name='직책')),
                ('department', models.CharField(blank=True, default='', max_length=50, verbose_name='부서')),
                ('direct', models.CharField(blank=True, default='', max_length=20, verbose_name='직통번호')),
                ('phone', models.CharField(blank=True, default='', max_length=20, verbose_name='유선전화')),
                ('mobile', models.CharField(blank=True, default='', max_length=20, verbose_name='휴대폰')),
                ('fax', models.CharField(blank=True, default='', max_length=30, verbose_name='팩스')),
                ('email', models.CharField(blank=True, default='', max_length=250, verbose_name='이메일')),
                ('address', models.TextField(blank=True, default='', verbose_name='주소')),
                ('eng_name', models.CharField(blank=True, default='', max_length=150, verbose_name='영문 이름')),
                ('eng_company_name', models.CharField(blank=True, default='', max_length=100, verbose_name='영문 회사명')),
                ('eng_position', models.CharField(blank=True, default='', max_length=100, verbose_name='영문 직책')),
                ('eng_deptment', models.CharField(blank=True, default='', max_length=50, verbose_name='영문 부서')),
                ('eng_address', models.TextField(blank=True, default='', verbose_name='영문 주소')),
                ('my_bc', models.BooleanField(verbose_name='본인명함 여부')),
                ('inquiry_date', models.DateTimeField(verbose_name='마지막 조회일')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='등록일')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='마지막 수정일')),
                ('book_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='BusinessCard', to='businesscardbook.businesscardbook')),
                ('ocr_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='BusinessCard', to='businesscardocr.businesscardocr')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='BusinessCard', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '명함',
                'verbose_name_plural': '명함 목록',
                'ordering': ['-create_date'],
            },
        ),
    ]
