from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=32,verbose_name="用户名")
    emial = models.EmailField(max_length=32,verbose_name="邮箱")

    class Meta:
        verbose_name_plural = "用户表"
    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=32,verbose_name="角色名")

    class Meta:
        verbose_name_plural ="角色表"
    def __str__(self):
        return self.name