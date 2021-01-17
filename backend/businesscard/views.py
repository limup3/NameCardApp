from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from .serializers import BusinessCardSerializer
from .models import BusinessCard


# Create your views here.
# views.py modify / 2020-11-04 Brian


class BusinessCardViewSet(viewsets.ModelViewSet):
    serializer_class = BusinessCardSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [OrderingFilter]
    ordering_fields = ["id", "create_date", "name", "company_name", "address", "inquiry_date"]
    ordering = ["id", "create_date", "name", "company_name", "address", "inquiry_date"]

    def get_queryset(self):
        queryset = BusinessCard.objects.all()
        useridparam = self.request.query_params.get("user_id", None)
        if useridparam is not None:
            queryset = queryset.filter(user_id=useridparam)
        bookidparam = self.request.query_params.get("book_id", None)
        if bookidparam is not None:
            queryset = queryset.filter(book_id=bookidparam)
        mybcparam = self.request.query_params.get("my_bc", None)
        if mybcparam is not None:
            queryset = queryset.filter(my_bc=mybcparam)
        ocridtypeparam = self.request.query_params.get("ocr_id_type", None)
        if ocridtypeparam is not None:
            queryset = queryset.filter(ocr_id__type=ocridtypeparam)
        ocridparam = self.request.query_params.get("ocr_id", None)
        if ocridparam is not None:
            queryset = queryset.filter(ocr_id=ocridparam)
        return queryset
