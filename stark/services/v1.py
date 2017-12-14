#!usr/bin/env python
# -*- coding:utf-8 -*-
from django.shortcuts import HttpResponse,render
from django.conf.urls import url

class StarkConfig(object):
    list_display = []
    def __init__(self,model_class,site):
        self.model_class = model_class
        self.site = site

    def get_urls(self):
        app_model_name = (self.model_class._meta.app_label,self.model_class._meta.model_name)
        url_patten = [
            url(r'^$',self.changelist_view,name="%s_%s_changelist"%app_model_name),
            url(r'^add/$',self.add_view,name="%s_%s_changelist"%app_model_name),
            url(r'^(\d+)/del/$',self.delete_view,name="%s_%s_changelist"%app_model_name),
            url(r'^(\d+)/change/$',self.change_view,name="%s_%s_changelist"%app_model_name),
        ]
        return url_patten
    @property
    def urls(self):
        return self.get_urls()

    # =============处理请求的方式方法=============
    def changelist_view(self,request,*args,**kwargs):
        '''
        列表展示页面
        /stark/app01/userinfo/    self.model_class = models.UserInfo
        /stark/app01/role/        self.model_class = models.Role
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        # ==============处理表头的数据==============
        head_list = []
        for field_name in self.list_display:
            if isinstance(field_name,str):
                verbose_name = self.model_class._meta.get_field(field_name).verbose_name
            else:
                verbose_name = field_name(self,is_header=True)
            head_list.append(verbose_name)

        # =============处理表中的数据============
        # list_display = ["id","name"]
        data_list = self.model_class.objects.all()
        # [
        #     ['id','name']
        #     ['id','name']
        # ]
        new_data_list = []
        for row in data_list:
            temp = []
            for field_name in self.list_display:
                if  isinstance(field_name,str):
                    val = getattr(row,field_name)
                else:
                    val = field_name(self,row)
                temp.append(val)
            new_data_list.append(temp)


        return render(request,"stark/changelist_view.html",{"data_list":new_data_list,"head_list":head_list})

    def add_view(self, request, *args, **kwargs):
        return HttpResponse("列表页面")

    def delete_view(self, request, *args, **kwargs):
        return HttpResponse("列表页面")

    def change_view(self, request, *args, **kwargs):
        return HttpResponse("列表页面")

class StarkSite(object):
    def __init__(self):
        self._registry = {}

    def register(self,model_class,stark_config_class = None):
        if not stark_config_class:
            stark_config_class = StarkConfig
        self._registry[model_class] = stark_config_class(model_class,self)

    def get_urls(self):
        url_patten = []
        for model_class,stark_config_obj in self._registry.items():
            '''为每一个类创建4个url'''
            app_name = model_class._meta.app_label
            model_name = model_class._meta.model_name
            print(app_name,model_name)
            curd_url = url(r'^%s/%s/'%(app_name,model_name),(stark_config_obj.urls,None,None))
            url_patten.append(curd_url)
        print(url_patten)
        return url_patten
    @property
    def urls(self):
        return (self.get_urls(),None,"stark")
site = StarkSite()