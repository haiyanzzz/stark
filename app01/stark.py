#!usr/bin/env python
# -*- coding:utf-8 -*-
print("sssssssss")
from stark.services import v1
from app01 import models
from django.utils.safestring import mark_safe
class UserInfoConfig(v1.StarkConfig):
    def edit(self,obj=None,is_header=False):
       if is_header:
          return "操作"
       return  mark_safe("<a href='/%s/edit'>编辑</a>"%(obj.id))

    def checkbox(self,obj=None,is_header=False):
        if is_header:
            return "选择"
        return mark_safe("<input type='checkbox' name='pk' value='%s'/>"%(obj.id))

    list_display = [checkbox,"id","name","emial",edit]
v1.site.register(models.UserInfo,UserInfoConfig)

class RoleConfig(v1.StarkConfig):
    def edit(self,obj=None,is_header=False):
       if is_header:
          return "操作"
       return  mark_safe("<a href='/%s/edit'>编辑</a>"%(obj.id))

    def checkbox(self,obj=None,is_header=False):
        if is_header:
            return "选择"
        return mark_safe("<input type='checkbox' name='pk' value='%s'/>"%(obj.id))

    list_display = [checkbox,"id","name",edit]
v1.site.register(models.Role,RoleConfig)
print(v1.site._registry)