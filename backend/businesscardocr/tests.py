# serializers.py create / 2020-11-08 Brian

from django.db.models.fields import BooleanField
from rest_framework import serializers
from .models import BusinessCardOcr
from drf_extra_fields.fields import Base64ImageField
from rest_framework import status
from rest_framework.response import Response
import requests
import base64
import json
from businesscard.models import BusinessCard
from django.conf import settings


class BusinessCardOcrSerializer(serializers.ModelSerializer):
    image = Base64ImageField()
    print("test1")
    class Meta:
        model = BusinessCardOcr
        fields = ("id", "image", "type", "user_id", "create_date", "update_date")
    def create(self, validated_data):
        print(validated_data)
        try:
            print("test2")
            request = self.context["request"]
            # request를 만든다
            invitations_data = request.data.get("my_bc")
            # 만든 request에서 장고에서 정해지지않은 리액트 변수 전달
            image = validated_data.pop("image")

            type = validated_data.pop("type")
            user_id = validated_data.pop("user_id")

            ocrData = BusinessCardOcr.objects.create(type=type, image=image, user_id=user_id)

            importOcrData = BusinessCardOcr.objects.get(id=ocrData.id)
            response = requests.post(
                f"{settings.OCRIMAGE_URL}{settings.PROJECT_URL}{settings.MEDIA_URL}{importOcrData.image}"
            )
            jsonOcrData = response.json().get("results").get("data")
            # print(jsonOcrData)
            del jsonOcrData["DEBUG"]
            for val in jsonOcrData.values():
                if val != "":
                    type = "Recognizing"
                    break
                else:
                    type = "Unrecognizable"

            if (
                jsonOcrData["이름"] != ""
                and jsonOcrData["회사명"] != ""
                and jsonOcrData["전화번호"] != ""
                and jsonOcrData["주소"] != ""
            ):
                type = "Success"

            importOcrData.type = type

            if type != "Unrecognizable":
                BusinessCard.objects.create(
                    name=jsonOcrData["이름"],
                    eng_name=jsonOcrData["영문이름"],
                    department=jsonOcrData["부서"],
                    eng_deptment=jsonOcrData["영문부서"],
                    position=jsonOcrData["직책"],
                    eng_position=jsonOcrData["영문직책"],
                    company_name=jsonOcrData["회사명"],
                    eng_company_name=jsonOcrData["영문회사명"],
                    address=jsonOcrData["주소"],
                    eng_address=jsonOcrData["영문주소"],
                    direct=jsonOcrData["직통"],
                    phone=jsonOcrData["전화번호"],
                    mobile=jsonOcrData["모바일"],
                    fax=jsonOcrData["팩스"],
                    email=jsonOcrData["이메일"],
                    my_bc=invitations_data,
                    user_id=importOcrData.user_id,
                    ocr_id=importOcrData,
                )

            importOcrData.save()
        except Exception as ex:  # 에러 종류
            print("에러가 발생 했습니다", ex)  # ex는 발생한 에러의 이름을 받아오는 변수

        return ocrData
