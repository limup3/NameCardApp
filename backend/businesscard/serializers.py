# serializers.py create / 2020-11-04 Brian

from rest_framework import serializers
from .models import BusinessCard


class BusinessCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessCard
        fields = "__all__"