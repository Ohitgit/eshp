from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django_summernote.fields import SummernoteTextField
# Create your models here.
class Category(models.Model):
     name=models.CharField(max_length=120,null=True)
     description=models.TextField(max_length=120,null=True)
           
     
class Subcategory(models.Model):
       subcategoryname=models.ForeignKey(Category,on_delete=models.CASCADE)

class Product(models.Model):
      categoryname=models.ForeignKey(Category,on_delete=models.CASCADE)
      title=models.CharField(max_length=50,null=True)
      slug=models.CharField(max_length=50,null=True)
      short=models.TextField(null=True)
      desc=models.TextField(null=True)
      product_image = models.ImageField(upload_to="product")


     
class Productspacefiacation(models.Model):
      productname=models.ForeignKey(Product,on_delete=models.CASCADE)
      spaceficationname=models.CharField(max_length=50,null=True)
      spaceficationvalue=models.CharField(max_length=50,null=True)



class BlogCategory(models.Model):
    code = models.CharField(max_length=10, null=True, blank=True)
    date=models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400,blank=True, null=True)
    slug = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.name) 

    

  

class BlogSubCategory(models.Model):
    code = models.CharField(max_length=10, null=True, blank=True)
    date=models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(BlogCategory,on_delete=models.CASCADE)
    description = models.CharField(max_length=400,blank=True, null=True)
    

    def __str__(self):
        return '{}'.format(self.name)
    


class Blog(models.Model):

    review_choices = (
        ('1', 'Pending'),
        ('2', 'Published'),
        ('3', 'Rejected'),
    )

    # blog_id = models.CharField(max_length=150, unique=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=10, null=True, blank=True)
    title= models.CharField(max_length=200, unique=True)
    short_dsc = models.CharField(max_length=250)
    dsc = models.TextField()
    dsc1 = models.TextField(blank=True,null=True)
    write= models.CharField(max_length=200, null=True)
    dsc2 = models.TextField(blank=True,null=True)
    siteengineer= models.CharField(max_length=200, null=True)
    siteengineerimg= models.ImageField(upload_to="blog",null=True)
    slug = models.CharField(max_length=550, default='title-with')
    category = models.ForeignKey(BlogCategory, on_delete=models.SET_NULL, null=True)
    subcategory = models.ForeignKey(BlogSubCategory,max_length=50, default="", on_delete=models.SET_NULL,null=True, blank=True)
    tags = TaggableManager()
    post_keywords = models.CharField(max_length=550)
    date = models.DateTimeField(auto_now_add=True, null=True)
    image= models.ImageField(upload_to="blog")
    image_caption = models.CharField(max_length=200, default='default-image-caption')
    review_status = models.CharField(max_length=1, choices=review_choices, default='2')

    def __str__(self):
        return '{}'.format(self.title)


class Contact(models.Model):
     name=models.CharField(max_length=120,null=True)
     email=models.CharField(max_length=120,null=True)
     phone=models.CharField(max_length=120,null=True)
     companyname=models.CharField(max_length=120,null=True)
     requirment=models.CharField(max_length=120,null=True)
     enquiry=models.CharField(max_length=120,null=True)

class Fileupload(models.Model):
      name=models.CharField(max_length=120,null=True)
      desc=models.TextField()
      upload=models.FileField(upload_to="doc")


class Testimonial(models.Model):
      desc=models.TextField(null=True)
      img=models.ImageField(upload_to="image")
      name=models.CharField(max_length=80,null=True)
      designation=models.CharField(max_length=80,null=True)


class Faq(models.Model):
      answer=models.CharField(max_length=80,null=True)
      question=models.TextField(null=True)




class Comment(models.Model):
      blog = models.ForeignKey(Blog, on_delete=models.CASCADE,null=True,related_name='comments')
      desc=models.TextField(null=True)
      name=models.CharField(max_length=80,null=True)
      email=models.CharField(max_length=80,null=True)
      website=models.CharField(max_length=80,null=True)
      date=models.DateTimeField(auto_now_add=True,null=True)

      def __str__(self):
        return '{}'.format(self.name)
class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
    author_name = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.author_name)
class About(models.Model):
      status = (
        ('1', 'Active'),
        ('2', 'Inactive'),
       )

      img= models.ImageField(upload_to="blog")
      img1= models.ImageField(upload_to="blog",null=True)
      img2= models.ImageField(upload_to="blog",null=True)
      content1=models.TextField(null=True)
      content2=models.TextField(null=True)
      content3=models.TextField(null=True)
      status = models.CharField(max_length=1, choices=status, default='2')
      date=models.DateTimeField(auto_now_add=True,null=True)



class Slide(models.Model):
     name=models.CharField(max_length=80,null=True)
     des=models.CharField(max_length=80,null=True)
     engineerimg= models.ImageField(upload_to="blog",null=True)
     engineerdesc= models.TextField(blank=True,null=True)



class Slide1(models.Model):
     name=models.CharField(max_length=80,null=True)
     des=models.CharField(max_length=80,null=True)
     engineerimg= models.ImageField(upload_to="blog",null=True)
     engineerdesc= models.TextField(blank=True,null=True)



