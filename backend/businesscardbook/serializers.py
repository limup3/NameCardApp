# serializers.py create / 2020-11-08 Brian

from rest_framework import serializers
from .models import BusinessCardBook


class BusinessCardBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessCardBook
        fields = "__all__"