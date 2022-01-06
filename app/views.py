from django.db.models import query
from django.db.models.fields import NullBooleanField
from django.http.request import QueryDict
from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render,HttpResponse
from django.views import View
from .forms import CustomerReg, ProfileReg
from .models import Customerinfo,Productinfo,Cart,OrderPlaceinfo
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required       #function based view
from django.utils.decorators import method_decorator            #class Based view

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
@method_decorator(login_required,name="dispatch")
class ProductDetailView(View):
    def get(self,request,pk):
        product=Productinfo.objects.get(pk=pk)
        itemAl=False
        itemAl=Cart.objects.filter(Q (product=product.id) & Q(user=request.user)).exists()
        return render(request, 'app/productdetail.html',{'product':product,'itemAl':itemAl})

@login_required
def add_to_cart(request):
    user=request.user
    product_id=request.GET.get('prod_id')
    product=Productinfo.objects.get(id=product_id)
    print(product)
    print(user)
    Cart(user=user,product=product).save()
    return redirect('/cart/')

@login_required
def show_cart(request):
    if request.user.is_authenticated:
        user=request.user
        cart=Cart.objects.filter(user=user)
        print(cart)
        amount=0.0
        shipping_amount=100.0
        total_amount=0.0
        cart_product=[p for p in Cart.objects.all() if p.user==user]
        print(cart_product)
        if cart_product:
            for p in cart_product:
                temp_amount=(p.quantity*p.product.discounted_price)
                amount+=temp_amount
                total_amount=amount+shipping_amount
            return render(request,'app/addtocart.html',{'crt':cart,'tt':total_amount,'am':amount})
        else:
            return render(request,'app/emptyCart.html')

@login_required
def plus_cart(request):
    if request.method=="GET":
        prod_id=request.GET['prod_id']
        c=Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity+=1
        c.save()
        user=request.user
        cart=Cart.objects.filter(user=user)
        amount=0.0
        shipping_amount=100.0
        total_amount=0.0
        cart_product=[p for p in Cart.objects.all() if p.user==user]
        print(cart_product)
        for p in cart_product:
                temp_amount=(p.quantity*p.product.discounted_price)
                amount+=temp_amount
                total_amount=amount+shipping_amount
        
        data={
                'quantity':c.quantity,
                'am':amount,
                'tt':total_amount
            }      
        return JsonResponse(data)

@login_required
def minus_cart(request):
    if request.method=="GET":
        prod_id=request.GET['prod_id']
        c=Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity-=1
        c.save()
        user=request.user
        cart=Cart.objects.filter(user=user)
        amount=0.0
        shipping_amount=100.0
        total_amount=0.0
        cart_product=[p for p in Cart.objects.all() if p.user==user]
        print(cart_product)
        for p in cart_product:
                temp_amount=(p.quantity*p.product.discounted_price)
                amount+=temp_amount
                total_amount=amount+shipping_amount
        
        data={
                'quantity':c.quantity,
                'am':amount,
                'tt':total_amount
            }      
        return JsonResponse(data)

@login_required
def remove_cart(request):
    if request.method=="GET":
        prod_id=request.GET['prod_id']
        c=Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        user=request.user
        cart=Cart.objects.filter(user=user)
        amount=0.0
        shipping_amount=100.0
        total_amount=0.0
        cart_product=[p for p in Cart.objects.all() if p.user==user]
        print(cart_product)
        for p in cart_product:
                temp_amount=(p.quantity*p.product.discounted_price)
                amount+=temp_amount
                total_amount=amount+shipping_amount
        
        data={
                'am':amount,
                'tt':total_amount
            }      
        return JsonResponse(data)


def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
    add=Customerinfo.objects.filter(user=request.user.id)
    return render(request,'app/address.html',{'add':add,'active':'btn-primary'})
    
@login_required
def orders(request):
    op=OrderPlaceinfo.objects.filter(user=request.user)
    return render(request,'app/orders.html',{'op':op})

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


#@method_decorator(login_required,name="dispatch")
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

@login_required
def checkout(request):
    user=request.user
    add=Customerinfo.objects.filter(user=user)
    cart_items=Cart.objects.filter(user=user)
    amount=0.0
    shipping_amount=100.0
    total_amount=0.0
    cart_product=[p for p in Cart.objects.all() if p.user==user]
    print(cart_product)
    if cart_product:
       for p in cart_product:
            temp_amount=(p.quantity*p.product.discounted_price)
            amount+=temp_amount
            total_amount=amount+shipping_amount
    return render(request, 'app/checkout.html',{'add':add,'tt':total_amount,'amount':amount,'crt':cart_items})

@login_required
def payment_doneView(request):
    user=request.user
    custid=request.GET.get('custid')
    customer=Customerinfo.objects.get(id=custid)
    cart=Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaceinfo(user=user,customer=customer,product=c.product,quantity=c.quantity).save()
        c.delete()
    return redirect("orders")
    

@method_decorator(login_required,name="dispatch")
class ProfileView(View):
    def get(self,request):
        form=ProfileReg()
        return render(request,'app/profile.html',{'form':form,'active':'btn-primary'})
    
    def post(self,request):
        form=ProfileReg(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request,'Congratulations:profile has been updated')
            return render(request,'app/profile.html',{'form':form})
        return render(request,'app/profile.html',{'form':form})

