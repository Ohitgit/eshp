from django.shortcuts import render, get_object_or_404, redirect
from dashboard.models import *
from django.core.paginator import Paginator
from django.conf import settings as conf_settings
from django.template.loader import render_to_string
from django.core.mail import send_mail 
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from .utils import *
from random import randint
from django.core.cache import cache
from django.http import  JsonResponse

# Create your views here.

def get_product_data():
    products = cache.get('all_products')
    if not products:
        
        products= list(Product.objects.select_related('categoryname').all())
        cache.set('all_products', products)
        print('-----data from cache ',products)
    return products

def home(request):
    prod=Product.objects.all()
    # ss=abc[0]
    # print('fff',ss.title)
    products=prod

    context = {
    
    'products':products,
    
    }
    return render(request, 'webapp/home.html',context)

# def get_slide_data():
#     slide = cache.get('slide')
#     if not slide:
        
#         slide= list(Slide.objects.all())
#         cache.set('slide', slide)
#     # print('-----data from cache silde ',slide)
#     return slide

# def get_about_data():
#     about = cache.get('all_about ')
#     if not about :
#         about= About.objects.get(status=1)
#         cache.set('all_about',about)
#     print('-----data from cache all_about ',about)
#     return about

def about(request):
    products=Product.objects.all()
    slide=Slide.objects.all()
    
    try:
        about=About.objects.get(status=1)
    except About.DoesNotExist:
           about=None
    context = {
    
    'products':products,
    'silde':slide,
    'silde1':Slide1.objects.all(),
    'about':about
   
    }
    return render(request, 'webapp/about.html',context)

def contact(request):
    products=Product.objects.all()
    
    context = {'products':products}
    try:
         if request.method =="POST":
              name=request.POST.get('name')
              email=request.POST.get('email')
              phone=request.POST.get('phone')
              company=request.POST.get('company')
              requirment=request.POST.get('requirment')
            
              enquiry=request.POST.get('enquiry')
              user=Contact.objects.create(name=name,email=email,phone=phone,companyname=company,requirment=requirment,enquiry=enquiry)
              messages.info(request,'Data inserted Succesfully')
           
              Util.contact_email(request,user)
    except Exception as e:
       print(e)
    return render(request, 'webapp/contact.html',context)




    
def blog(request):
    return render(request, 'webapp/blog.html')
def quartz(request):
    return render(request, 'webapp/quartz.html')
def feldspar(request):
    return render(request, 'webapp/feldspar.html')
def clay(request):
    return render(request, 'webapp/clay.html')
def granite(request):
    return render(request, 'webapp/granite.html')
def limestone(request):
    return render(request, 'webapp/limestone.html')

def get_faq_data():
    faq = cache.get('all_faq')
    if not faq:
        
        faq= Faq.objects.all()
        cache.set('all_faq', faq)
    print('-----data from cache faq ',faq)
    return faq

def faq(request):
    faq=Faq.objects.all()
    products=Product.objects.all()
    context = {
            'faq':faq,
           'products':products,
       }
    return render(request,'webapp/faq.html',context)
 
def team(request):
    return render(request,'webapp/team.html')


def get_testimonial_data():
    testimonial = cache.get('all_testimonial')
    if not testimonial:
        
        testimonial= Testimonial.objects.all()
        cache.set('all_testimonial',testimonial)
    print('-----data from cache testimonial ',testimonial)
    return testimonial

def testimonial(request):
    products=Product.objects.all()
    testmonial=Testimonial.objects.all()
    context = {
           'testmonial':testmonial,
           'products':products,
       }
    return render(request,'webapp/testimonials.html',context) 

def features(request):
    return render(request,'webapp/feature.html') 

def pricing(request):
    return render(request,'webapp/pricing.html')  


def all_blog(request):
    products=Product.objects.all()
    try:
        blogs=Blog.objects.all()
        paginator = Paginator(blogs, 5)
        page_number = request.GET.get('page')
        blog = paginator.get_page(page_number)
        context = {
          'blog': blog,
          'page_range': paginator.page_range,
          'products':products
       }
    except Exception as e:
            print(e)
    return render(request,'webapp/all_blog.html',context)

def get_comment_data():
    comment = cache.get('all_comment')
    if not comment:
        
        comment= Comment.objects.all()
        cache.set('all_comment',comment)
    print('-----data from cache testimonial ',comment)
    return comment

def blog_detail(request,slug):
    comment=Comment.objects.all()
    abc=Blog.objects.values_list()
    for x in abc:
     print('ddd',x[0])

    context = {
        'products':Product.objects.all(),
        'blog':Blog.objects.get(slug=slug),
        'blogs':Blog.objects.all(),
        'comment':comment,
        'reply':Reply.objects.all(),
        }
    return render(request,'webapp/blog_detail.html',context)


def add_comment(request ,post_id,slug):
    blog= get_object_or_404(Blog, id=post_id)
    bloger=Blog.objects.get(slug=slug)

    if request.method =="POST":
        name=request.POST.get('name')
        desc=request.POST.get('message')
        email=request.POST.get('email')
        website=request.POST.get('website')
        comment=Comment.objects.create(blog=blog,desc=desc,name=name,email=email,website=website)
        comment.save()
       
        return redirect('blog_detail',slug=bloger.slug)
def product(request,slug):
    context={
        'products':Product.objects.filter(slug=slug)
         }

    return render(request,'webapp/products.html',context)


def add_reply(request, comment_id,slug):
    comment = get_object_or_404(Comment, id=comment_id)
    blog=Blog.objects.get(slug=slug)
    if request.method == 'POST':
        author_name = request.POST['author_name']
        content = request.POST['content']
        reply = Reply.objects.create(comment=comment, author_name=author_name, content=content)
        reply.save()
       
        return redirect('blog_detail',slug=blog.slug)


def custom_404(request, exception):
    return render(request, '404.html')




def check(request):
    
    page_data = PageData.objects.all()

    if request.method == 'POST':
        is_checked1 = request.POST.get('checkbox_name')
        print('is',is_checked1)
        page_data1 = PageData.objects.filter(is_checked=False)
        print('ggg',page_data1)
        # page_data2 = PageData.objects.create(is_checked=True)
        # print('ff',page_data1)
        
        if is_checked1 !="off":
            # Checkbox is checked, do something
            # page_data.is_checked = True
            # page_data.save()
              print('on')
              page_data1.delete()
              

        else:
             print('off')
            # page_data2.is_checked = False
            # page_data2.save()
            # Checkbox is unchecked, delete the data
            
            
        

    return render(request, 'check.html', {'page_data': page_data})
