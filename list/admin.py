from django.contrib import admin

from list.models import CustomUser, Chat
from list.models import Task

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Task)
admin.site.register(Chat)
