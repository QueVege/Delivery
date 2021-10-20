from app.models import (
    Transport, Company, Driver
)
from app.serializers import (
    TransportSerializer, CompanySerializer, DriverSerializer
)
from rest_framework import generics, viewsets
from rest_framework.generics import get_object_or_404



class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

    def get_queryset(self):
        return Driver.objects.filter(company__id=self.kwargs['comp_pk'])


class TransportListAPI(generics.ListCreateAPIView):
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['pk'] = self.kwargs['pk']
        return context

    def get_queryset(self):
        company = get_object_or_404(Company, id=self.kwargs['pk'])
        return Transport.objects.filter(company=company)

    def perform_create(self, serializer):
        company = get_object_or_404(Company, id=self.kwargs['pk'])
        return serializer.save(company=company)


class DriverDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


class DriverListAPI(generics.ListCreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

    def get_queryset(self):
        company = get_object_or_404(Company, id=self.kwargs['pk'])
        return Driver.objects.filter(company=company)

    def perform_create(self, serializer):
        company = get_object_or_404(Company, id=self.kwargs['pk'])
        return serializer.save(company=company)


class TransportDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer

