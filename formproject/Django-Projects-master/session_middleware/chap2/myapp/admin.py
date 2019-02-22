from django.contrib import admin
from .models import *

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','email','post','created','active')
    list_filter = ('active','created','updated')
    search_field =('name','email','body')
    
# Register your models here.
admin.site.register(Post)
admin.site.register(Comment,CommentAdmin)

