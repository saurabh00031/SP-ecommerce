from django.contrib import admin
from .models import Customerinfo,Productinfo,Cart,OrderPlaceinfo

@admin.register(Customerinfo)
class CustomerDisp(admin.ModelAdmin):
    list_display=['id','user','name','locality','city','zipcode','state']

@admin.register(Productinfo)
class ProductDisp(admin.ModelAdmin):
    list_display=['id','title','selling_price','discounted_price','description','description','brand','category','product_image']

@admin.register(Cart)
class CartDisp(admin.ModelAdmin):
    list_display=['id','user','product','quantity']

@admin.register(OrderPlaceinfo)
class OrderPlaceDisp(admin.ModelAdmin):
    list_display=['id','user','customer','product','quantity','ordered_date','status']


