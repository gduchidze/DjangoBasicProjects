from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.http import Http404

# Create your views here.

def index(request):
    return HttpResponse("<h5> this is bitcamp.ge </h5>")

def main_page(request):
    return HttpResponse("<h1> THIS IS MAIN PAGE </h1>")

def article(request,year):
    return HttpResponse(f"<h2>ARTICLE YEAR: {year} </h2>")

products = ["Bread","Milk","Eggs","Apples"]
my_dict = {"name":"Giorgi",
           "company":"bitcamp"
           }

def category(request):
    # x = render_to_string('myapp/index.html')
    # return HttpResponse(x)
    data = {'title': 'BITCAMP_TITLE',
            'products': products,
            'my_dict': my_dict,
            'set': {1,2,3,3},
            'float':25.433,
            }

    return render(request, 'myapp/index.html',data)

def student(request,id):
    if id > 20:
        return redirect('/articles/2004',permanent=True)
    return HttpResponse(f"<h1>student id: {id} </h1> <p>fsfsd </p>")

def page_not_found(request, exception):
    return HttpResponseNotFound(f"<h1>page not found </h1>")