from django.urls import path
from .views import homeView, shopView, blogView, aboutView, contactView, cartView, productdetailView, addcartView, \
    addcartprdView, removecartView, emailUpdate, addcarthomeView

app_name = 'e_commerce'

urlpatterns = [
    path('', homeView, name='home'),
    path('home/addcart/<int:id>/', addcarthomeView, name='addcarthome'),
    path('shop/', shopView, name='shop'),
    path('shop/pdetail/<int:id>/', productdetailView, name='pdetail'),
    path('shop/addcart/<int:id>/', addcartprdView, name='addcartprd'),
    path('blog/', blogView, name='blog'),
    path('about/', aboutView, name='about'),
    path('contact/', contactView, name='contact'),
    path('email/', emailUpdate, name='emailupdate'),
    path('cart/', cartView, name='cart'),
    path('cart/addcart/<int:id>/', addcartView, name='addcart'),
    path('cart/removecart/<int:id>/', removecartView, name='removecart'),
]
