from django.contrib import admin
from .models import Post,Shop,Calender


myModels = [Post, Shop, Calender]
admin.site.register(myModels)
