from django.contrib import admin
from .models import Thread, ThreadAction, ThreadMember

admin.site.register(Thread)
admin.site.register(ThreadMember)
admin.site.register(ThreadAction)

# Register your models here.
