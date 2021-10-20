from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app import views


router = DefaultRouter()
router.register(r'companies', views.CompanyViewSet, basename='company')

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += [
    path(
        'companies/<int:pk>/transport/',
        views.TransportListAPI.as_view(),
        name='transport-list'
    ),
    path(
        'transport/<int:pk>',
        views.TransportDetailAPI.as_view(),
        name='transport-detail'
    ),
    path(
        'companies/<int:pk>/drivers/',
        views.DriverListAPI.as_view(),
        name='driver-list'
    ),
    path(
        'drivers/<int:pk>',
        views.DriverDetailAPI.as_view(),
        name='driver-detail'
    ),
]

