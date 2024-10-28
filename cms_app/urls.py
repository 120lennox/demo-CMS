from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PageViewSet, SectionViewSet

router = DefaultRouter()
router.register(r'pages', PageViewSet)
router.register(r'sections', SectionViewSet)

urlpatterns = [
    path('', include(router.urls))
]