from django.core import paginator
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Project
# from . forms import  ProjectPurchase
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# from django.core.mail import send_mail

        


def project_list(request, category_slug=None):
    """ 
    A fuction that would show a list of available projects 
    And project category
    """
    category = None
    categories = Category.objects.all()
    projects = Project.objects.filter(available=True)
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        projects = projects.filter(category=category)
  
    # PAGINATOR 
    paginator = Paginator(projects, 8) # 10 Projects in each page
    page = request.GET.get('page')
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an interger deliver the first page
        projects = paginator.page(1)
    except EmptyPage:
        # if page is out of range deliver last page of results
        projects = paginator.page(paginator.num_pages)
        
        
    return render(request, 
                  'project/index.html',
                  {'category':category,
                  'categories':categories,
                  'projects':projects,
                  'page':page,
                  'section':'projects',
                  'section':'category'})
    

def project_detail(request, id, slug):
    """ Display project's Detail """
    project = get_object_or_404(Project,
                                id=id,
                                slug=slug,
                                available=True)
    return render(request,
                  'project/detail.html',
                  {'project':project})


def search(request):
    """ Fuction that cares about searching of a project topic """
    q=request.GET['q']
    projects = Project.objects.filter(name__icontains=q)
    data = Project.objects.filter(name__icontains=q).order_by('-created')
    return render(request, 'project/search.html', {'data':data,
                                                   'projects':projects})