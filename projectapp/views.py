from django.shortcuts import render, get_object_or_404
from .models import Category, Project, Purchase, Wishlist, Plan, UserGuid
from . forms import Customerform
from django.views.generic.edit import CreateView




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
    guids = UserGuid.objects.all()
    plans = Plan.objects.all()
    context = {'guids':guids,
               'plans':plans}
    return render(request, 'project/guide.html', context)


def user_wishlist(request):
    form = Customerform()
    if request.method=='POST':
        form = Customerform(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request,'project/wish.html', context)

class PurchaseCreateView(CreateView):
    model = Purchase
    form_class = 'ProjectPurchase'
    template_name = "project/purchase.html"
