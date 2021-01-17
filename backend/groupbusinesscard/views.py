from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from .serializers import GroupBusinessCardSerializer
from .models import GroupBusinessCard


# Create your views here.
# views.py modify / 2020-11-08 Brian

class GroupBusinessCardViewSet(viewsets.ModelViewSet):
    serializer_class = GroupBusinessCardSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [OrderingFilter]
    ordering_fields = ['id']
    ordering = ['id']

    def get_queryset(self):
        queryset = GroupBusinessCard.objects.all()
        useridparam = self.request.query_params.get("user_id", None)
        if useridparam is not None:
            queryset = queryset.filter(user_id=useridparam)
        return queryset






