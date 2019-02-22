from django.contrib import admin
from .models import *
from django.contrib.auth.models import User, Group


admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.register(Employee)
admin.site.register(College)
admin.site.register(Student)
admin.site.register(Book)

admin.site.site_header = "Hello World"
admin.site.site_title = "UMSRA Admin Portal"
admin.site.index_title = "Welcome to UMSRA Researcher Portal"

