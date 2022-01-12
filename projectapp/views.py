from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Comment, Project, Purchase, Plan, Wishlist
from . forms import Customerform, CommentForm, SharebyEmail
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.core.mail import send_mail



def projectShare(request, project_id):
    # Retrive project by id
    project = get_object_or_404(Project, id=project_id, active=True)
    sent = True
    if request.method == 'POST':
        form = SharebyEmail(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            project_url = request.build_absolute_uri(
                project.get_absolute_url())
            subject = f"{cd['name']} Recommeds you to buy {project.name}" 
            message = f"Download {project.name} at {project.url}\n\n" \
                        f"{cd['name']}\'s comments: {cd['comments']}"
            send_mail(subject, message, 'belloyusuf@gmail.com', [cd['to']])
            sent = True
    else:
        form = SharebyEmail()
    return render(request, 'project/share.html',
                  {'project':project,
                   'form':form,
                   'sent':'sent'})
        
        


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
    return render(request, 
                  'project/index.html',
                  {'category':category,
                  'categories':categories,
                  'projects':projects,
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


def user_wishlist(request):
    """ function that would handle a use wishlist """
    wishlist = Wishlist.objects.all()
    if request.method=='POST':
        form = Customerform(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, "Wish project is submitted successfully")
            # return redirect('wishlist/')
    else:
        form = Customerform()
    context = {'form':form,
               'wishlist':wishlist,
               'section':'user_wishlist'}
    return render(request,'project/wish.html', context)


# comment function
def user_comment(request):
    """ A form that would take care of user's coment """
    comments = Comment.objects.filter(active=True)
    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, "Thanks for your feedback")
    else:
        form = CommentForm()
    return render(request, 'project/comment.html',
                    {'comments':comments,
                    'form':form,
                    'section':'comment'})



class PurchaseCreateView(CreateView):
    """ Class that would handle a purchase form"""
    model = Purchase
    form_class = 'ProjectPurchase'
    template_name = "project/purchase.html"
