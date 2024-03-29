from django.urls import path
from app import views
from .forms import PasswordChangeReg
from .forms import CustomerReg
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from app.forms import LoginReg

urlpatterns = [
    #path('', views.home),
    path('',views.ProductView.as_view(),name="home"),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/',views.show_cart,name="showcart"),
    path('buy/', views.buy_now, name='buy-now'),
    path('pluscart/',views.plus_cart,name="pluscart"),
    path('minuscart/',views.minus_cart,name="minuscart"),
    path('removecart/',views.remove_cart,name="removecart"),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('passwordchange/',auth_view.PasswordChangeView.as_view(template_name="app/passwordchange.html",form_class=PasswordChangeReg,success_url="/passwordchangedone/"),name="passwordchange"),
    path('passwordchangedone/',auth_view.PasswordChangeView.as_view(template_name="app/passwordchangedone.html"),name="passwordchangedone"),
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile,name='mobiledata'),
    path('accounts/login/', auth_view.LoginView.as_view(template_name='app/login.html',authentication_form=LoginReg), name='login'),
    path('logout/',auth_view.LogoutView.as_view(next_page='login'),name='logout'),
    path('registration/', views.CustomerView.as_view(), name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
    path('paymentdone/', views.payment_doneView, name='paymentdone'),
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
