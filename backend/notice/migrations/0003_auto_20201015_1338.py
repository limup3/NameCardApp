# Generated by Django 3.1.2 on 2020-10-15 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0002_auto_20201015_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='update_date',
            field=models.DateTimeField(auto_now=True, verbose_name='마지막 수정일'),
        ),
    ]
