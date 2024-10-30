from django.shortcuts import render
from rest_framework import viewsets
from .models import Page, Section
from .serializers import PageSerializer, SectionSerializer

# Create your views here.
class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    lookup_field = 'slug'

class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer