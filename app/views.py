from django.db.models.fields import NullBooleanField
from django.shortcuts import render,HttpResponse
from django.views import View
from .forms import CustomerReg
from .models import Customerinfo,Productinfo,Cart,OrderPlaceinfo

#def home(request):
 #return render(request, 'app/home.html')

class ProductView(View):
    def get(self,request):
        topwears=Productinfo.objects.filter(category='TW')
        bottomwears=Productinfo.objects.filter(category='BW')
        mobiles=Productinfo.objects.filter(category='M')
        laptops=Productinfo.objects.filter(category='L')
        craze={

          "topwears":topwears,
          "bottomwears":bottomwears,
          "mobiles":mobiles,
          "laptops":laptops
        }
        return render(request, 'app/home.html',craze)



#def product_detail(request):
 #return render(request, 'app/productdetail.html')

class ProductDetailView(View):
    def get(self,request,pk):
        product=Productinfo.objects.get(pk=pk)
        return render(request, 'app/productdetail.html',{'product':product})


def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request,data=None):
    if data == None:
        mobiles=Productinfo.objects.filter(category='M')
    elif data=='karbonn' or data=='apple' or data=='samsung':
        mobiles=Productinfo.objects.filter(category="M").filter(brand=data)
    elif data=="below":
        mobiles=Productinfo.objects.filter(category="M").filter(discounted_price__lt=10000)
        if mobiles==None:
            return HttpResponse(request,"no such filters available")
    elif data=="above":
        mobiles=Productinfo.objects.filter(category="M").filter(discounted_price__gt=10000)
        if mobiles==None:
            return HttpResponse(request,"no such filters available")    
    return render(request, 'app/mobile.html',{'mobiles':mobiles})



class CustomerView(View):
    def get(self,request):
        form=CustomerReg()
        return render(request,'app/customerregistration.html',{'form':form})
    def post(self,request):
        form=CustomerReg(request.POST)
        if form.is_valid:
            form.save()
            return render(request,'app/customerregistration.html',{'form':form})
        return render(request,'app/customerregistration.html',{'form':form})


def checkout(request):
 return render(request, 'app/checkout.html')
