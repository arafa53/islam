from django.contrib import admin
from .models import BlogComment, Post,Contact,Item
from django.contrib import admin
# Register your models here.



admin.site.register((Post,BlogComment,Contact,Item))

