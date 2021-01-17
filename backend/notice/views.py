from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import NoticeSerializer
from .models import Notice

# Create your views here.


class NoticeViewSet(viewsets.ModelViewSet):
    serializer_class = NoticeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Notice.objects.all()
        titleparam = self.request.query_params.get("title", None)
        if titleparam is not None:
            queryset = queryset.filter(title=titleparam)
        return queryset

