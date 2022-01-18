from django.core import paginator
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Comment, Project, Purchase, Plan, Wishlist
from . forms import Customerform, CommentForm, ProjectPurchase
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
   
def UserGuid_detail(request):
    plans = Plan.objects.all()
    context = {'plans':plans,
               'section':'UserGuid_detail'}
    return render(request, 'project/guide.html', context)

@login_required
def user_wishlist(request):
    """ function that would handle a use wishlist """
    wishlist = Wishlist.objects.all()
    if request.method=='POST':
        form = Customerform(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, "Thanks for telling us your wish project")
            # return redirect('wishlist/')
    else:
        form = Customerform()
    context = {'form':form,
               'wishlist':wishlist,
               'section':'user_wishlist'}
    return render(request,'project/wish.html', context)


# comment function
@login_required
def user_comment(request):
    """ A form that would take care of user's coment """
    comments = Comment.objects.filter(active=True)
    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, "Thanks for your comment")
    else:
        form = CommentForm()
    return render(request, 'project/comment.html',
                    {'comments':comments,
                    'form':form,
                    'section':'comment'})


def purchaseProject(request):
    project = Project.objects.filter(available=True)
    if request.method == 'POST':
        form = ProjectPurchase(request.POST)
        if form.is_valid():
            # cd = form.cleaned_data
            form.save()
            return redirect('comment/')
            # messages.add_message(request, messages.SUCCESS, "Your project topic would be sent to you via your Email Address")
    else:
        form = ProjectPurchase()
    return render(request, 'project/purchase.html',
                      {'form':form,
                       'project':project})