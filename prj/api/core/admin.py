from django.contrib import admin
from .models import autoDriveModel
# Register your models here.
# 为core子应用配置相应的后台管理功能
admin.site.register(autoDriveModel) # 注册定义好的模型