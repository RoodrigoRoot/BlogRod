from django.shortcuts import render
from post.models import Post
from account.models import Profile
from django.views import View
# Create your views here.

class IndexView(View):
    
    def get(self, request, *args, **kwargs):
        
        posts = Post.objects.all()
        author = Profile.objects.first()
        
        return render(request, 'Post/posts.html', locals())