from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.views.generic import ListView , DetailView
from django.views.generic.edit import UpdateView
from django.http import HttpResponse
from datetime import date
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.db.models import F
from django.contrib.auth.decorators import login_required
from .models import *
import random
# Create your views here.

def index(request):
    context={}
    context['ref']=Reference.objects.all()
    context['last_news']=News.objects.all().order_by('-publishing_date')[:3]
    context['product_3']=Product.objects.all().order_by('-publishing_date')[:3]
    disc = Discount_Product.objects.all()
    images = Cover_image.objects.all()
    if len(images) > 0:
        context['images'] = images[0]
    if len(disc) > 0:
        context['discount']=disc[0]
        
    about = About.objects.all().distinct()
    if not len(about) == 0:
        context['about_con'] = about[0]
        
    bulk_order = Bulk_Order_Product.objects.all().distinct()   
    if not len(bulk_order) == 0:
        context['bulk_order'] = bulk_order[0]
        
    return render(request,'index.html',context)

def about(request):
    context2={}
    
    about = About.objects.all().distinct()
    if not len(about) == 0:
        context2['about_con'] = about[0]
        
    context2['staff'] = Team_Member.objects.all()
    context2['product_3']=Product.objects.all().order_by('-publishing_date')[:3]
    return render(request,'about.html',context2)

def contact(request):
    context3={}
    about = About.objects.all().distinct()
    if not len(about) == 0:
        context3['about_con'] = about[0]
    if request.method=="POST":
        
        username=request.POST.get('name')
        mail=request.POST.get('email')
        number=request.POST.get('tel')
        comment=request.POST.get('message')
        subject=request.POST.get('subject')
        result = int(request.POST.get('a')) + int(request.POST.get('b'))
        if result == int(request.POST.get('result')):
        
            make_comment = Connection.objects.create(Name=username,mail=mail, tel=number, Content=comment,Subject=subject)
            make_comment.save()
            
        else:
            a = random.randint(1,100)
            b = random.randint(1,10)
            context3['a']=a
            context3['b']=b
            context3['username']=username
            context3['email']=mail
            context3['tel']=number
            context3['message']=comment
            context3['konu']=subject
            context3['error'] = 'İşlem sonucu yanlış. Lütfen sonucu doğru giriniz!'
            return render(request,'contact.html',context3)
            
            
    a = random.randint(1,100)
    b = random.randint(1,10)
    context3['a']=a
    context3['b']=b
    context3['product_3']=Product.objects.all().order_by('-publishing_date')[:3]
    
        
    
    return render(request,'contact.html',context3)


def news(request):
    context4={}
    context4['product_3']=Product.objects.all().order_by('-publishing_date')[:3]
    about = About.objects.all().distinct()
    if not len(about) == 0:
        context4['about_con'] = about[0]
    posts=News.objects.filter(Q(completed__iexact='completed')).order_by('-publishing_date').distinct()
    date_search=request.GET.get('date')
    category_search=request.GET.get('category')
    if date_search:
        posts= posts.filter(
             Q(date__exact=date_search)
        ).distinct()
        
    if category_search:
        posts= posts.filter(
             Q(category__name__exact=category_search)
        ).distinct()
    
    """   paginator start  """
    paginator = Paginator(posts,61) # bir sayfada kaç tane görünmesi gerek
    context4['filter_count']=paginator.count
    page_num = request.GET.get('page')
    page=paginator.get_page(page_num)
    
    context4['count']=paginator.count
    context4['page'] = page  
    page_number=page.number

    if page_number !=None:
        fark=int(paginator.num_pages) - int(page_number)
       
        if fark >= 2:
            context4['last'] = ('last')
            if fark > 2:
                context4['last_three'] = ('last_three')
                
            
        if int(page_number) >= 3:
            context4['first'] = ('first')
            
            if int(page_number) > 3:
                context4['three_dot'] = ('three_dot')
            
    else:

        
        if paginator.num_pages-1 >= 2:
            context4['last_true'] = ('last')
            if paginator.num_pages-1 >2:
                
                context4['last_three'] = ('last_three')
    
    """   paginator end  """

    return render(request,'news.html',context4)


def single_news(request, slug):
    context5={}
    the_news=get_object_or_404(News, slug=slug)
    about = About.objects.all().distinct()
    if not len(about) == 0:
        context5['about_con'] = about[0]
    date_arşiv = []
    archives = []
    context5['the_news']=the_news
    context5['news']=News.objects.all()
    
    for i in News.objects.filter(Q(completed__iexact='completed')).order_by('-publishing_date').distinct():
        if i.date not in date_arşiv:
            date_arşiv.append(i.date)
    
    for i in date_arşiv:
        postss = News.objects.filter(date = i)
        archives  += [[i,len(postss)]]
            

    context5['archive']=archives
    context5['last_news']=News.objects.filter(Q(completed__iexact='completed')).order_by('-publishing_date').distinct()[:5]
    context5['product_3']=Product.objects.all().order_by('-publishing_date')[:3]
    context5['cat']=News_Category.objects.all()
    """ comment """
    
    if request.method=="POST":
        
        username=request.POST.get('name')
        mail=request.POST.get('email')
        comment=request.POST.get('comment')
        result = int(request.POST.get('a')) + int(request.POST.get('b'))
        if result == int(request.POST.get('result')):
        
            make_comment = Comments.objects.create(post = the_news, name=username, email=mail, content=comment)
            make_comment.save()
            
        else: 
            a = random.randint(1,100)
            b = random.randint(1,10)
            context5['a']=a
            context5['b']=b
            context5['username']=username
            context5['email']=mail
            context5['message']=comment
            context5['error'] = 'İşlem sonucu yanlış. Lütfen sonucu doğru giriniz!'
            return render(request,'single-news.html',context5)
            
            
    a = random.randint(1,100)
    b = random.randint(1,10)
    context5['a']=a
    context5['b']=b
    
    
    """ comment end """
    
    return render(request,'single-news.html',context5)


def single_product(request, slug):
    context6={}
    about = About.objects.all().distinct()
    if not len(about) == 0:
        context6['about_con'] = about[0]
    context6['the_product']=get_object_or_404(Product, slug=slug)
    context6['allproducts']=Product.objects.all().order_by('-publishing_date')[:3]
    return render(request,'single-product.html',context6)



def handle_not_found(request, exception):
    context7={}
    about = About.objects.all().distinct()
    if not len(about) == 0:
        context7['about_con'] = about[0]
        
    context7['allproducts']=Product.objects.all().order_by('-publishing_date')[:3]  
        
    return render(request, '404.html',context7)



