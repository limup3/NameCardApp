# serializers.py create / 2020-10-14 robert

from rest_framework import serializers
from .models import Notice


class NoticeSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = Notice
        fields = "__all__"
