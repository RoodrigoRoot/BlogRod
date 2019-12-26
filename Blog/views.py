from django.views import View
from django.shortcuts import redirect, render
from Article.models import Article

class IndexView(View):

    def get(self, request, *args, **kwargs):
        article = Article.objects.last()      
        
        return render(request, "index.html", locals())

