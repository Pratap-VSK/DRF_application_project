from django.contrib import admin
from .models import Blog, Comment

admin.sie.register(Blog)
admin.site.register(Comment)