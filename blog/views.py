from django.shortcuts import render, get_object_or_404

#need to access jobs from db and display
from .models import Blog

# Create your views here.
def allblogs(request):
    blogs = Blog.objects #now turned into Python objects that can be used
    return render(request, 'blog/allblogs.html', {'blogs':blogs})
    #routes to blog/allblogs.html in blog template folder

def detail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk = blog_id) #Blog is the model in the database
    return render(request, 'blog/detail.html',{'blog':detailblog})

    #main url->blog url->blog/int->sets blog id->
    #calls views.detail function (in views.py)->function returns detail.html
