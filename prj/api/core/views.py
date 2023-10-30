from rest_framework import viewsets
from .serializers import modelSerializer
from .models import autoDriveModel

# Create your views here.
# 自定义模型的添加、删除、查询和修改
class modelViewSet(viewsets.ModelViewSet):
    serializer_class=modelSerializer
    queryset=autoDriveModel.objects.all()