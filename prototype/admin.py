from django.contrib import admin
from .models import players

# Register your models here.

# class playersAdmin(admin.ModelAdmin):
#     # list_display = (("lastName","firstName","bbox","birthPlace"))
#     prepopulated_fields = {"slug":("lastName","firstName")}
# admin.site.register(players, playersAdmin) #adminページから、playerテーブルを操作できるようにする。


admin.site.register(players) #adminページから、playerテーブルを操作できるようにする。
