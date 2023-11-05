from django.db import models

# 在Django模型中，每个模型类对应数据库中的一张表
# Create your models here.
class autoDriveModel(models.Model):
    name=models.CharField(max_length=120,verbose_name='名称')
    description=models.TextField(max_length=400,verbose_name='描述')
    input_video=models.FileField(verbose_name='源数据')
    output_video=models.FileField(verbose_name='测试结果')
    
    

    class Meta: # 定义了autoDriveModel的元数据
        verbose_name = "模型" # 单数形式
        verbose_name_plural = "模型" # 复数形式

    def __str__(self): # 定义了一个对象转化为字符串时应该怎样显示
        return self.name