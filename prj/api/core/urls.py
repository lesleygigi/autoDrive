from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import modelViewSet

# router 自动生成路由
# /autoDrive/：创建POST/GET
# 

router=DefaultRouter()
router.register(r'autoDriveModels',modelViewSet)

urlpatterns = [
    path('',include(router.urls)),
]
