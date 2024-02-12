

from django.contrib import admin
from django.urls import path,include,re_path
from . import views


urlpatterns = [
   path('',views.home,name='web_home'),
   path('about',views.about,name='about'),
   path('blog',views.blog,name='blog'),
   path('products/<slug:slug>/',views.product,name='products'),
   path('contact',views.contact,name='contact'),
   path('quartz',views.quartz,name='quartz'),
   path('feldspar',views.feldspar,name='feldspar'),
   path('clay',views.clay,name='clay'),
   path('limestone',views.limestone,name='limestone'),
   path('granite',views.granite,name='granite'),
   path('our-team',views.team,name='team'),
   path('faq',views.faq,name='faq'),
   path('features',views.features,name='features'),
   path('all-blog',views.all_blog,name='all_blog'),
   path('blog-detail/<slug:slug>/',views.blog_detail,name='blog_detail'),
   path('add-comment/<int:post_id>/<slug:slug>/',views.add_comment,name='add_comment'),
   path('add-reply/<int:comment_id>/<slug:slug>/',views.add_reply,name='add_reply'),
   path('pricing',views.pricing,name='pricing'),
   path('check',views.check,name='check'),
   path('testimonial',views.testimonial,name='testimonial'),
 
 



]    