from django.apps import AppConfig


class StarkConfig(AppConfig):
    name = 'stark'

    def ready(self):
        from django.utils.module_loading import autodiscover_modules
        autodiscover_modules('stark')   #stark和应用里面自己创建的模块的名字要对应上