# serializers.py create / 2020-11-08 Brian

from rest_framework import serializers
from .models import GroupBusinessCard


class GroupBusinessCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupBusinessCard
        fields = "__all__"