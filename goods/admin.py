from django.contrib import admin

from goods.models import Goods, Option, Provider, Shipping


# Register your models here.

admin.site.register(Goods)
admin.site.register(Option)
admin.site.register(Provider)
admin.site.register(Shipping)