from django.shortcuts import render
from django.views import View 
from django.http import HttpResponse
from urllib import request 
from . models import Product
from django.db.models import Count
from . forms import CustomerRegistrationForm
from django.contrib import messages
# Create your views here.
def home(request):
   return render(request,"app/home.html")




class CategoryView(View):   
    def get(self, request,val):
        product=Product.objects.filter(category=val)
        title=Product.objects.filter(category=val).values('title') 
        return render(request, "app/categorie.html",locals())



class ProductDetails(View):
    def get(self,request,pk):
        product=Product.objects.get(pk=pk)
        return render (request,"app/productdetails.html",locals())



class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        return render(request,'app/Customerregistration.html',locals())
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Congratulations ! User Register Successfully")
        else:
            messages.warning(request,"Invalid Input Data")
        return render(request,'app/Customerregistration.html',locals())