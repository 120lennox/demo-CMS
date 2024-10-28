from rest_framework import serializers
from .models import Page, Section

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ('id', 'name', 'content', 'order')

class PageSerializer(serializers.ModelSerializer):
    sections = SectionSerializer(many=True, read_only=True)

    class Meta:
        model = Page
        fields = [
            'id', 
            'title',
            'slug',
            'content',
            'is_published',
            'created_at', 
            'updated_at',
            'sections',
        ]