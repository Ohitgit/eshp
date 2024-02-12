from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.http.response import JsonResponse
from django.contrib import messages
from .models import *
from django.core.mail import send_mail ,EmailMultiAlternatives
from django.conf import settings
from django.core.paginator import Paginator
# Create your views here.
# def category(request):
#    notes =Notes.objects.all()
#    #pagination
#    # pg=Paginator(notes,2)
#    # page_num=request.GET.get('page')
#    # notesfinal=pg.get_page(page_num)
#    #serach filter
#    # if request.method=="GET":
#    #     st=request.GET.get('note')
#    #     if st!=None:
#    #         notes=Notes.objects.filter(notes=st)

#    data={'notes':notes}
#    return render(request,"notes/notes.html",data)

def store(request):
    category=Category.objects.all()
    pro=Product.objects.all()
    if request.method=="POST":
        cat=request.POST.get('cat')
        notes=request.POST.get('notes')
        description=request.POST.get('description')
        catobj=Category.objects.get(id=cat)
        Notes.objects.create(notes=notes,description=description,cat=catobj)
        messages.info(request, "Notes add")
        return redirect('/')
    return render(request,"notes/store.html",{'category':category,'pros':pro})

def edit(request,pk):
    notes = Notes.objects.get(id=pk)
    if request.method=="POST":
      notes.notes=request.POST.get('notes')
      notes.description=request.POST.get('description')
      notes.save()
      messages.info(request, "Notes Update")
      return  redirect('/')
    return render(request, "notes/edit.html", {'notes': notes})

def delete(request,pk):
    notess=Notes.objects.get(id=pk)
    notess.delete()
    messages.info(request, "Notes Delete")
    return  redirect('/')

def practice(request):
    list=["apple","mango","grapes"]
    return render(request,'practice.html',{'list':list})



def emails(request):
    if request.method=="POST":
        msg=request.POST.get('mssg')
        name=request.POST.get('name')
        email=request.POST.get('email')
        send_mail('Contact Form',
                  msg,settings.EMAIL_HOST_USER,[email],fail_silently=False
                  )
    return render(request,'email/email.html')


def productprice(request):
    if request.method=='POST':
       cat=request.POST.get('cat')
       pro=request.POST.get('pro')
       sub=Notes.objects.filter(cat=cat,pro=pro).first()
       print(sub.notes)
       return JsonResponse({'status':True})
    return redirect('/')

def dependentfield(request):
    countrys=Country.objects.all()
    countryid=request.GET.get('country',None)
    stateid = request.GET.get('state',None)
    state=None
    district=None
    if countryid:
        getcoun=Country.objects.get(id=countryid)
        state=State.objects.get(id=getcoun)
    if stateid:
        getstate =State.objects.get(id=stateid)
        district = State.objects.get(id=getstate)
    return render(request,'country/depnd.html',locals())
