from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from .serializers import BusinessCardBookSerializer
from .models import BusinessCardBook


# Create your views here.
# views.py modify / 2020-11-08 Brian

class BusinessCardBookViewSet(viewsets.ModelViewSet):
    serializer_class = BusinessCardBookSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [OrderingFilter]
    ordering_fields = ['id']
    ordering = ['id']

    def get_queryset(self):
        queryset = BusinessCardBook.objects.all()
        useridparam = self.request.query_params.get("user_id", None)
        if useridparam is not None:
            queryset = queryset.filter(user_id=useridparam)
        groupidparam = self.request.query_params.get("group_id", None)
        if groupidparam is not None:
            queryset = queryset.filter(group_id=groupidparam)
        return queryset




