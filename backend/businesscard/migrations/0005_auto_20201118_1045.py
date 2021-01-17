# Generated by Django 3.1.3 on 2020-11-18 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('businesscardbook', '0001_initial'),
        ('businesscard', '0004_auto_20201106_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businesscard',
            name='book_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='BusinessCard', to='businesscardbook.businesscardbook'),
        ),
    ]
