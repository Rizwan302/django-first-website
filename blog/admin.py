from django.contrib import admin
from blog.models import Post,BlockComment

# Register your models here.
admin.site.register((BlockComment))

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('tinyInject.js',)
