from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'transaction', views.TransactionView)

urlpatterns = [
    path('', include(router.urls)),
]
