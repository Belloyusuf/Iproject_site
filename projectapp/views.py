from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Project, Purchase, Plan
from . forms import Customerform
from django.views.generic.edit import CreateView
from django.contrib import messages




def project_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    projects = Project.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        projects = projects.filter(category=category)
    return render(request, 
                  'project/index.html',
                  {'category':category,
                  'categories':categories,
                  'projects':projects})


def project_detail(request, id, slug):
    project = get_object_or_404(Project,
                                id=id,
                                slug=slug,
                                available=True)
    return render(request,
                  'project/detail.html',
                  {'project':project})


def search(request):
    q=request.GET['q']
    projects = Project.objects.filter(name__icontains=q)
    data = Project.objects.filter(name__icontains=q).order_by('-created')
    return render(request, 'project/search.html', {'data':data,
                                                   'projects':projects})
   
   
def UserGuid_detail(request):
    plans = Plan.objects.all()
    context = {'plans':plans}
    return render(request, 'project/guide.html', context)


def user_wishlist(request):
    if request.method=='POST':
        form = Customerform(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, "Added successfully")
            return redirect('/project/UserGuid_detail/')
    else:
        form = Customerform()
    context = {'form':form}
    return render(request,'project/wish.html', context)



class PurchaseCreateView(CreateView):
    model = Purchase
    form_class = 'ProjectPurchase'
    template_name = "project/purchase.html"
