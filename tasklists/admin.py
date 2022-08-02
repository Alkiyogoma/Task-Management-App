from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Users)
admin.site.register(Task)
admin.site.register(TaskType)
admin.site.register(TaskComment)
admin.site.register(TaskUser)
admin.site.site_header='Albo Admin Panel'
#admin.site.site_title='Albogast'
