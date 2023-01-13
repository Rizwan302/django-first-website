from django.contrib import admin
from project.models import MyProject
# Register your models here.


@admin.register(MyProject)
class MyProjectAdmin(admin.ModelAdmin):
    class Media:
        js= ('tinyInject.js',)

