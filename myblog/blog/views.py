from django.shortcuts import render

# Create your views here.

def blog_view(request):
    blog_titles = ['Blog post 1', 'Blog post 2', 'Blog post 3', 'Blog post 4']

    data = {"blog_names" : blog_titles}
    
    return render(request, 'blog/index.html', data)