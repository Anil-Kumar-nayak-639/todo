from django.contrib import admin
from todoapp.models import todolist
# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display=['list','done']
    list_per_page=10
    list_filter = ('manage',)

admin.site.register(todolist,TodoAdmin)
