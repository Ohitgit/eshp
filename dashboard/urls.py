from django.urls import path
from dashboard import views


urlpatterns = (

path('',views.index,name='dashboard_home'),
path('category/',views.category,name='category'),
path('category-update/<int:id>',views.category_delete,name='category_delete'),
path('category-delete/<int:id>',views.category_update,name='category_update'),
path('subcategory/',views.subcategory,name='subcategory'),
path('subcategory-delete/<int:id>',views.subcategory_delete,name='subcategory_delete'),
path('subcategory-update/<int:id>',views.subcategory_update,name='subcategory_update'),
path('product/',views.product,name='product'),
path('product-delete/<int:id>',views.product_delete,name='product_delete'),
path('product-update/<int:id>',views.product_update,name='product_update'),
path('productspace/',views.product_space,name='product_space'),
path('productspace-del/<int:id>',views.product_space_del,name='product_space_del'),
path('productspace-update/<int:id>',views.product_space_update,name='product_space_update'),
path('dashboard/',views.dashboard,name='dashboard'), 
path('blogcategory/',views.Blogcategory,name='blogcategory'), 
path('blogcategory-update/<int:id>',views.Blogcategory_update,name='blogcategory_update'), 
path('blogcategory-delete/<int:id>',views.Blogcategory_delete,name='Blogcategory_delete'), 
path('blogsubcategory/',views.Blogsubcategory,name='blogsubcategory'), 
path('blogsubcategory-update/<int:id>',views.Blogsubcategory_update,name='blogsubcategory_update'), 
path('blogsubcategory-delete/<int:id>',views.Blogsubcategory_delete,name='Blogsubcategory_delete'), 
path('blogs/',views.blog,name='blogs'),
path('blog-update/<int:id>',views.blog_update,name='blog_update'),
path('blog-delete/<int:id>',views.blog_delete,name='blog_delete'),
path('product-specifiy',views.product_specifiy,name='product_specifiy'),
path('file',views.file,name='file'),
path('file-update/<int:id>',views.file_update,name='file_update'),
path('file-delete/<int:id>',views.file_delete,name='file_delete'),
path('testmonials',views.testmonial,name='testmonials'),
path('testmonials-update/<int:id>',views.testmonial_update,name='testmonial_update'),
path('testmonials-delete/<int:id>',views.testmonial_delete,name='testmonial_delete'),
path('faqs',views.faq,name='faqs'),
path('faqs-update/<int:id>',views.faq_update,name='faq_update'),
path('faqs-delete/<int:id>',views.faq_delete,name='faq_delete'),
path('abouts/',views.abouts,name='abouts'),
path('about-update/<int:id>',views.about_update,name='about_update'),
path('cms/',views.cms,name='cms'), 

    
    
)