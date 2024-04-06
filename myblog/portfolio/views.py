from django.shortcuts import render, redirect

# Create your views here.

def contact_view(request):
    if request.method == 'POST':
        return redirect('allgood')
    return render(request, 'portfolio/contact.html')

def allgood_view(request):
    return render(request, 'portfolio/allgood.html')

def projects_view(request):
    projects = [
        {'name': 'TODO app', 'description': "The coolest todo web application in the world"},
        {'name': 'Airbnb Clone', 'description': "hdfg Clone, that's 123it..."},
        {'name': 'amazon Clone', 'description': "hdfgh Clone, that'ghs it..."},
        {'name': 'mymarket', 'description': "gsdfg Clone, that'dhfghdfs it..."},
        {'name': 'Instagram', 'description': "hd Clone, dhfghd's it..."},

    ]
    
    
    return render(request, 'portfolio/projects.html', {"projects": projects})