# 序列化器是Django Rest Framework提供的功能，能够
# 方便地将Django数据模型序列化成相应的JSON数据格式

from rest_framework import serializers
from .models import autoDriveModel

class modelSerializer(serializers.ModelSerializer):
    class Meta:
        model=autoDriveModel # 指定模型
        fields=( # 选择相应的字段展示
            'id',
            'name',
            'description',
            'input_video',
            'output_video'
        )