from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Wishlist, Plan, Comment, Purchase
from .forms import Customerform, CommentForm, ProjectPurchase 
from projectapp.models import Category, Project
from django.core.files.storage import FileSystemStorage



#  WISHLIST PROJECTS
def user_wishlist(request):
    categories = Category.objects.all()
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
               'categories':categories,
               'section':'user_wishlist'}
    return render(request,'content/wish.html', context)


# USER GUID AND OUR PLANS AND PRICE
def UserGuid_detail(request):
    categories = Category.objects.all()
    plans = Plan.objects.all()
    context = {'plans':plans,
               'categories':categories,
               'section':'UserGuid_detail'}
    return render(request, 'content/guide.html', context)


# USER COMMENTS OF PROJECTS
def user_comment(request):
    """ A form that would take care of user's coment """
    categories = Category.objects.all()
    comments = Comment.objects.filter(active=True)
    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user_comment = Comment(
                name=cd['name'],
                project=cd['project'],
                email=cd['email'],
                body=cd['body']
            )
            
            user_comment.save()
            messages.add_message(request, messages.INFO, "Thanks for your comment")
    else:
        form = CommentForm()
    return render(request, 'content/comment.html',
                    {'comments':comments,
                    'form':form,
                    'categories':categories,
                    'section':'comment'})


# USER PURCHASE FUNCTION
def purchaseProject(request):
    categories = Category.objects.all()
    project = Project.objects.filter(available=True)
    if request.method == 'POST':
        form = ProjectPurchase(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            user_purchase =  Purchase(
                project_course = cd['project_course'],
                project_name = cd['project_name'],
                email = cd['email'],
                phone = cd['phone'],
                upload_image=cd['upload_image'])
            user_purchase.save()
            messages.add_message(request, messages.SUCCESS, "Your project topic would be sent to you via your Email Address")
            return redirect('/content/done/')
    else:
        form = ProjectPurchase()
    return render(request, 'content/purchase.html',
                      {'form':form,
                       'categories':categories,
                       'project':project})

# Purchase done function
def purchaseDone(request):
    """ After user filling the purchase form"""
    project = Project.objects.filter(available=True)
    category = Category.objects.all()
    user_info = Purchase.objects.all()
    return render(request, 
                  'content/purchase_done.html', 
                  {'user_info':user_info,
                   'project':project,
                   'category':category})
    

    

