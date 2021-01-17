from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import BusinessCardOcrSerializer
from .models import BusinessCardOcr


# Create your views here.
# views.py modify / 2020-11-08 Brian


class BusinessCardOcrViewSet(viewsets.ModelViewSet):
    serializer_class = BusinessCardOcrSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = BusinessCardOcr.objects.all()
        typeparam = self.request.query_params.get("type", None)
        if typeparam is not None:
            queryset = queryset.filter(type=typeparam)
        useridparam = self.request.query_params.get("user_id", None)
        if useridparam is not None:
            queryset = queryset.filter(user_id=useridparam)
        return queryset
