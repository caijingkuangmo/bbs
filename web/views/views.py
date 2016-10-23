from django.shortcuts import render
import web.models
# Create your views here.
def index(request):
    articles = web.models.Article.objects.all()
    return render(request, 'index.html',{'articles':articles})

def category(request,category_id):
    print '***',request.path
    articles = web.models.Article.objects.filter(category_id = category_id)
    return render(request, 'home.html',{'articles':articles})

def home(request):
    print '***',request.path
    articles = web.models.Article.objects.all()
    return render(request, 'home.html',{'articles':articles})