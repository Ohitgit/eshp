from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
admin.site.register(Category)
admin.site.register(Subcategory)

admin.site.register(Productspacefiacation)
admin.site.register(BlogCategory)
admin.site.register(BlogSubCategory)
admin.site.register(Blog)

admin.site.register(Contact)
admin.site.register(Fileupload)
admin.site.register(About)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(Slide)
admin.site.register(Slide1)

class ProductAdmin(SummernoteModelAdmin):
    model = Product
    summernote_fields = ('desc',)
    list_display = ('title','slug','short','product_image',)
    

admin.site.register(Product,ProductAdmin)