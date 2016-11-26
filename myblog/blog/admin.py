from django.contrib import admin
from .models import Post,Shop


myModels = [Post, Shop]
admin.site.register(myModels)
