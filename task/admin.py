from django.contrib import admin
from .models import Profile, Tag, Task, Attachment
# Register your models here.
admin.site.register(Attachment)
admin.site.register(Profile)
admin.site.register(Task)
admin.site.register(Tag)
