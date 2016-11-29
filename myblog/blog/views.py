from django.utils import timezone
from django.shortcuts import render
from .models import Post
from .models import Shop,Calender

def post_list(request):
   posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
   return render(request, 'post_list.html', {'posts': posts})

def shop(request):
     shops = Shop.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
     return render(request, 'shop.html', { 'shops': shops})

def about(request):
    return render(request, 'about.html')

def blog(request):
   posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
   return render(request, 'blog.html', {'posts': posts})

def calender(request):
    dates = Calender.objects.filter(timing__lte=timezone.now()).order_by('timing')
    return render(request, 'calender.html', {'dates': dates})
