from django.shortcuts import render ,redirect
from django.contrib import messages
from .models import *
# Create your views here.
def index(request):
    return render(request,'dashboard/index.html')

def dashboard(request):
    return render(request,'dashboard/dashboard.html')

def cms(request):
    return render(request,'dashboard/cms.html')

def category(request):
    category=Category.objects.all()
    if request.method=='POST':
        name=request.POST.get('name')
        desc=request.POST.get('description')
        Category.objects.create(name=name,description=desc)
        messages.info(request,'Data inserted Succesfully')
    
    return render(request,'dashboard/category.html',{'category':category})

def category_delete(request,id):
    cat=Category.objects.get(id=id)
    cat.delete()
    return redirect('category')
     
def category_update(request,id):
     cat =Category.objects.get(id=id)
     if request.method=="POST":
      cat.name=request.POST.get('name')
      cat.description=request.POST.get('description')
      cat.save()
      messages.info(request, "Category Update")
      return  redirect('category')
    

def subcategory(request):
    category=Category.objects.all()
    subcategory=Subcategory.objects.all()
    if request.method=='POST':
        sub=request.POST.get('sub')
        catobj=Category.objects.get(id=sub)
        Subcategory.objects.create(subcategoryname=catobj)
        messages.info(request,'Data inserted Succesfully')
    return render(request,'dashboard/subcategory.html',{'category':category,'subcategory':subcategory})

def subcategory_delete(request,id):
    cat=Subcategory.objects.get(id=id)
    cat.delete()
    return redirect('subcategory')

def subcategory_update(request,id):
      sub =Subcategory.objects.get(id=id)
      if request.method=='POST':
        sub1=request.POST.get('sub')
        sub.subcategoryname=Category.objects.get(id=sub1)
        sub.save()
        messages.info(request,'Data inserted Succesfully')
        return redirect('subcategory')
      
def product(request):
    prods=Product.objects.all()
    cat=Category.objects.all()
    if request.method=='POST':
        prod = Product()
        prod.title=request.POST.get('name')
        prod.slug=request.POST.get('slug')
        cat=request.POST.get('cat')
        prod.short=request.POST.get('short')
        prod.categoryname=Category.objects.get(id=cat)
        prod.product_image=request.FILES['img']
        prod.save()
        
        messages.info(request,'Data inserted Succesfully')
    return render(request,'Dashboard/product.html',{'cat':cat,'prods':prods})

def product_delete(request,id):
    cat=Product.objects.get(id=id)
    cat.delete()
    return redirect('product')

def product_update(request,id):
      prod =Product.objects.get(id=id)
      print(prod)
      if request.method=='POST':
        prod.title=request.POST.get('name')
        prod.slug=request.POST.get('slug')
        prod.short=request.POST.get('short')
        cat=request.POST.get('cat')
        prod.categoryname=Category.objects.get(id=cat)
        prod.product_image=request.FILES['img']
        prod.save()
        messages.info(request,'Data inserted Succesfully')
        return redirect('product')
      
def product_space(request):
    pro_space=Productspacefiacation.objects.all()
    
    pros=Product.objects.all()
    
    if request.method=='POST':
        pro=request.POST.get('proname')
        prod_obj=Product.objects.get(id=pro)
        name=request.POST.getlist('name')
      
        value=request.POST.getlist('value')
        print('name1',name,'value1',value)
        for name1,value1 in zip(name,value):
            print('name1',name1,'value1',value1)
            Productspacefiacation.objects.create(productname=prod_obj,spaceficationname=name1,spaceficationvalue=value1)
        return redirect('product_space')       
        
        # total=request.POST.get('total')
        
        # for i in range(int(total)+1):
        #         print('-----------sub------',i)
                
        #         name = request.POST.get('name'+str(i))
        #         value = request.POST.get('Value'+str(i))
        #         print('-----------value------',value,symbol)
        #         try:
        #             Productspacefiacation.objects.create(productname=prod_obj,spaceficationname=name,spaceficationvalue=value)
        #             messages.info(request,'Data inserted Succesfully')
        #             # cat = CampaignSubCategory.objects.create(symbol=symbol ,category_id=category,value=value)
        #             # cat.save()
        #         except:
        #             pass
     
        
        
    return render(request,'Dashboard/productspace.html',{'pros':pros,'pro_space':pro_space})

def product_space_del(request,id):
    cat=Productspacefiacation.objects.get(id=id)
    cat.delete()
    return redirect('product_space')

def product_space_update(request,id):
      prod =Productspacefiacation.objects.get(id=id)
      if request.method=='POST':
        pro1=request.POST.get('proname')
        prod.productname=Product.objects.get(id=pro1)
        prod.spaceficationname=request.POST.get('name')
        prod.spaceficationvalue=request.POST.get('value')
        prod.save()
        messages.info(request,'Data inserted Succesfully')
        return redirect('product_space')


def Blogcategory(request):
    
    try:
        blog=BlogCategory.objects.all()
        if request.method=='POST':
          name=request.POST.get('name')
          code=request.POST.get('code')
          date=request.POST.get('date')
          description=request.POST.get('description')
          slug=request.POST.get('slug')
          BlogCategory.objects.create(name=name,code=code,date=date,description=description,slug=slug)
          messages.info(request,'Data inserted Succesfully')
          return redirect('blogcategory')

    except Exception as e:
        print(e)
    return render(request,'Dashboard/blogcategory.html',{'blog':blog})

def Blogcategory_update(request,id):
     prod =BlogCategory.objects.get(id=id)
     if request.method=='POST':
        prod.name=request.POST.get('name')
        prod.code=request.POST.get('code')
        prod.date=request.POST.get('date')
        prod.description=request.POST.get('description')
        prod.slug=request.POST.get('slug')
        prod.save()
        messages.info(request,'Data inserted Succesfully')
        return redirect('blogcategory')
     
def Blogcategory_delete(request,id):
    cat=BlogCategory.objects.get(id=id)
    cat.delete()
    return redirect('blogcategory')

def Blogsubcategory(request):
    cat=BlogCategory.objects.all()
    blog=BlogSubCategory.objects.all()
    if  request.method=="POST":
          name=request.POST.get('name')
          code=request.POST.get('code')
          date=request.POST.get('date')
          description=request.POST.get('description')
          cat=request.POST.get('cat')
          cat1=BlogCategory.objects.get(id=cat)
          BlogSubCategory.objects.create(name=name,code=code,date=date,description=description,category=cat1)
          messages.info(request,'Data inserted Succesfully')
          return redirect('blogsubcategory')
    return render(request,'Dashboard/blogsubcategory.html',{'blog':blog,'cat':cat})


def Blogsubcategory_update(request,id):
     
     prod =BlogSubCategory.objects.get(id=id)
     if request.method=='POST':
        prod.name=request.POST.get('name')
        prod.code=request.POST.get('code')
        prod.date=request.POST.get('date')
        prod.description=request.POST.get('description')
        cat=request.POST.get('cat')
        cat1=BlogCategory.objects.get(id=cat)
        prod.category=cat1
        prod.save()
        messages.info(request,'Data inserted Succesfully')
        return redirect('blogsubcategory')
     
def Blogsubcategory_delete(request,id):
    cat=BlogSubCategory.objects.get(id=id)
    cat.delete()
    return redirect('blogsubcategory')

def blog(request):
    user=User.objects.all()
    cat=BlogCategory.objects.all()
    subcat=BlogSubCategory.objects.all()
    blog=Blog.objects.all()
    if request.method=="POST":
          user1=request.POST.get('user')
          user2=User.objects.get(id=user1)

          title=request.POST.get('title')
          code=request.POST.get('code')
          date=request.POST.get('date')
          slug=request.POST.get('slug')
          description=request.POST.get('description')
          shortdescription=request.POST.get('shortdescription')
          blogimage=request.FILES['img']
          caption=request.POST.get('caption')
          keyword=request.POST.get('keyword')
          tags=request.POST.get('tags')
          cat=request.POST.get('cat')
          subcat=request.POST.get('subcat')
          review=request.POST.get('review')
          cat1=BlogCategory.objects.get(id=cat)
          subcat1=BlogSubCategory.objects.get(id=subcat)
          Blog.objects.create(title=title,code=code,date=date,dsc=description,slug=slug,short_dsc=shortdescription,image=blogimage,image_caption=caption,post_keywords=keyword,tags=tags,review_status=review,category=cat1,subcategory=subcat1,user_id=user2)
          messages.info(request,'Data inserted Succesfully')

    return render(request,'Dashboard/blog.html',{'blog':blog,'user':user,'cat':cat,'subcat':subcat})


def blog_update(request,id):
    blogs=Blog.objects.get(id=id)
    if request.method=='POST':
        blogs.title=request.POST.get('title')
        blogs.code=request.POST.get('code')
        blogs.date=request.POST.get('date')
        blogs.slug=request.POST.get('slug')
        blogs.dsc=request.POST.get('description')
        blogs.short_dsc=request.POST.get('shortdescription')
        blogs.image=request.FILES['img']
        blogs.image_caption=request.POST.get('caption')
        blogs.post_keywords=request.POST.get('keyword')
        blogs.tags=request.POST.get('tags')
        cat=request.POST.get('cat')
        subcat=request.POST.get('subcat')
        blogs.review_status=request.POST.get('review')
        cat1=BlogCategory.objects.get(id=cat)
        subcat1=BlogSubCategory.objects.get(id=subcat)
        user1=request.POST.get('user')
        user2=User.objects.get(id=user1)
        blogs.category=cat1
        blogs.subcategory=subcat1
        blogs.user_id=user2
        blogs.save()
        messages.info(request,'Data inserted Succesfully')
        return redirect('blog')
    
def blog_delete(request,id):
      cat=Blog.objects.get(id=id)
      cat.delete()
      return redirect('blog')


def product_specifiy(request):
     pro_space=Productspecifiy.objects.all()
    
     pros=Product.objects.all()
    
     if request.method=='POST':
        proname=request.POST.get('proname')
        product=Productspecifiy(products=proname)
        product.save()
        name=request.POST.getlist('name')
        for  names in name:
            v=Spacename(spacname=names)
            v.save()
            product.name.add(v)

        value=request.POST.getlist('value')
        for values in value:
            v=Spacevalue(spacevalue=values)
            v.save()
            product.value.add(v)
            return redirect('product_specifiy')

     return render(request,'Dashboard/productspace.html',{'pros':pros,'pro_space':pro_space})



def file(request):
    blog=Fileupload.objects.all()
    try:
        if request.method == 'POST':
            name=request.POST.get('name')
            desc=request.POST.get('desc')
            upload=request.FILES['upload']
            Fileupload.objects.create(name=name,desc=desc,upload=upload)
            messages.info(request,'Data inserted Succesfully')
            return redirect('file')
    except Exception as e:
          print(e)
    return render(request,'Dashboard/file.html',{'blog':blog}) 


def file_update(request,id):
    try:
        file=Fileupload.objects.get(id=id)
        if request.method == 'POST':
            file.name=request.POST.get('name')
            file.desc=request.POST.get('desc')
            file.upload=request.FILES['upload']
            file.save()
            messages.info(request,'Data inserted Succesfully')
            
    except Exception as e:
         print(e)
    return redirect('file')


def file_delete(request,id):
      cat=Fileupload.objects.get(id=id)
      cat.delete()
      return redirect('blog')

def testmonial(request):
     blog=Testimonial.objects.all()
     try:
        if request.method == 'POST':
            name=request.POST.get('name')
            desc=request.POST.get('desc')
            img=request.FILES['img']
            designation=request.POST.get('designation')
            Testimonial.objects.create(name=name,desc=desc,img=img,designation=designation)
            messages.info(request,'Data inserted Succesfully')
            return redirect('testmonials')
     except Exception as e:
          print(e)
     return render(request,'Dashboard/testmonial.html',{'blog':blog}) 



def testmonial_update(request,id):
    try:
        file=Testimonial.objects.get(id=id)
        if request.method == 'POST':
            file.name=request.POST.get('name')
            file.desc=request.POST.get('desc')
            file.img=request.FILES['img']
            file.designation=request.POST.get('designation')
            file.save()
            messages.info(request,'Data inserted Succesfully')
            
    except Exception as e:
         print(e)
    return redirect('testmonials')



def testmonial_delete(request,id):
      cat=Testimonial.objects.get(id=id)
      cat.delete()
      return redirect('testmonials')

def faq(request):
     blog=Faq.objects.all()
     try:
        if request.method == 'POST':
            answer=request.POST.get('answer')
            question=request.POST.get('question')
            Faq.objects.create(answer=answer,question=question)
            messages.info(request,'Data inserted Succesfully')
            return redirect('faqs')
     except Exception as e:
          print(e)
     return render(request,'Dashboard/faq.html',{'blog':blog}) 



def faq_update(request,id):
    try:
        file=Faq.objects.get(id=id)
        if request.method == 'POST':
            file.answer=request.POST.get('answer')
            file.question=request.POST.get('question')
           
            file.save()
            messages.info(request,'Data inserted Succesfully')
            
    except Exception as e:
         print(e)
    return redirect('faqs')


def faq_delete(request,id):
      cat=Faq.objects.get(id=id)
      cat.delete()
      return redirect('faqs')

def abouts(request):
     blog=About.objects.all()
     if request.method == 'POST':
      
        img= request.FILES.get('img')
        img1= request.FILES.get('img1')
        img2= request.FILES.get('img2')
        content=request.POST.get('content')
        content1=request.POST.get('content1')
        content2=request.POST.get('content2')
        content3=request.POST.get('content3')
        status=request.POST.get('status')
        About.objects.create(img=img,content=content,content1=content1,content2=content2,content3=content3,img1=img1,img2=img2,status=status)
        messages.info(request,'Data inserted Succesfully')
     return render(request,'Dashboard/about.html',{'blog':blog})


def about_update(request,id):
    try:
        file=About.objects.get(id=id)
        if request.method == 'POST':
            file.img= request.FILES.get('img')
            file.img1= request.FILES.get('img1')
            file.img2= request.FILES.get('img2')
            file.content=request.POST.get('content')
            file.content1=request.POST.get('content1')
            file.content2=request.POST.get('content2')
            file.content3=request.POST.get('content3')
            file.status=request.POST.get('status')
            file.save()
            messages.info(request,'Data inserted Succesfully')
            
    except Exception as e:
         print(e)
    return redirect('abouts')