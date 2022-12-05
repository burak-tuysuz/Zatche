from django.shortcuts import render
from django.http.response import HttpResponse
from blog.models import Blog,Category
# Create your views here.




def indexa(request):
    return HttpResponse("homepage")

def index(request):
    
    return render(request,"blog/index.html")

def planets(request):
    context = {
        "blogs" : Blog.objects.filter(),
        "categories" : Category.objects.all()
    }
    return render(request, "blog/planets.html",context)

def planet_category(request,slug):
        context = {
        "blogs" : Blog.objects.filter(category__slug = slug),
        "categories" : Category.objects.all(),
        "selected_category": slug
        }
        return render(request, "blog/planets.html",context)

def galaxies(request):
    return render(request, "blog/galaxies.html")

def blog_details(request,slug):
    blog = Blog.objects.get(slug=slug)
    return render(request, "blog/blog-details.html",{
        "blog" : blog
    })
