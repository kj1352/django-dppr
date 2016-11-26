from django.utils import timezone
from django.shortcuts import render
from .models import Post
from .models import Shop

def post_list(request):
   posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
   shops = Shop.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
   return render(request, 'post_list.html', {'posts': posts, 'shops': shops})

