from django.shortcuts import render
from django.http.response import HttpResponse
from blog.models import Blog,Category,Type
# Create your views here.



def index(request):
    
    return render(request,"blog/index.html")





def planets(request):
    context = {
        "blogs" : Blog.objects.filter(type = 4),
        "categories" : Category.objects.filter(type = 4),
        
        
    }
    print(context)
    return render(request, "blog/planets.html",context)

def categories(request,slug):
        print(slug)
        if (str(Category.objects.get(slug = slug).type) == "planet"):

            context = {
            "blogs" : Blog.objects.filter(category__slug = slug, type = 4),
            "categories" : Category.objects.filter(type = 4),
            "selected_category": slug,
            
            }

            return render(request, "blog/planets.html",context)

        elif (str(Category.objects.get(slug = slug).type) == "star"):
            context = {
            "blogs" : Blog.objects.filter(category__slug = slug, type = 5),
            "categories" : Category.objects.filter(type = 5),
            "selected_category": slug,
            
            }

            return render(request,  "blog/stars.html",context)

        else:
            context = {
            "blogs" : Blog.objects.filter(category__slug = slug, type = 6),
            "categories" : Category.objects.filter(type = 6),
            "selected_category": slug,
            
            }

            return render(request,"blog/galaxies.html",context)



def stars(request):
    context = {
        "blogs" : Blog.objects.filter(type = 5  ),
        "categories" : Category.objects.filter(type = 5),
        
    }

    return render(request, "blog/stars.html",context)






def galaxies(request):
    context = {
        "blogs" : Blog.objects.filter(type = 6),
        "categories" : Category.objects.filter(type = 6),
        
    }
    return render(request, "blog/galaxies.html",context)


def blog_details(request,slug):
    blog = Blog.objects.get(slug=slug)
    return render(request, "blog/blog-details.html",{
        "blog" : blog
    })
