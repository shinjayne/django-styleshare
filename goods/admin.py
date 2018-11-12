from django.contrib import admin

from goods.models import Goods, Option, Shipping


# Register your models here.

admin.register(Goods)
admin.register(Option)
admin.register(Shipping)