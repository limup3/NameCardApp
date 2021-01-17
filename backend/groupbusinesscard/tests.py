from django.test import TestCase

# serializers.py create / 2020-11-08 Brian

from rest_framework import serializers
from .models import BusinessCardOcr
from drf_extra_fields.fields import Base64ImageField
from rest_framework import status
from rest_framework.response import Response
import requests
import base64
import json
from businesscard.models import BusinessCard
from .models import GroupBusinessCard
from django.conf import settings


class GroupBusinessCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupBusinessCard

    def create(self, validated_data):
        print(type(self))


# Create your tests here.
