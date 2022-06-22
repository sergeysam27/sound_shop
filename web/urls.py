from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about.html', views.about, name='about'),
    path('shop.html', views.ProductsListView.as_view(), name='shop'),
    path('<int:pk>.html', views.ProductsDetailView.as_view(), name='product'),
    path('cart.html', views.cart_view, name='cart'),
    path('checkout.html', views.checkout, name='checkout'),
    path('contact.html', views.contact, name='contact'),
    path('login.html', views.login_user, name='login'),
    path('register.html', views.RegisterView.as_view(), name='register'),
    path('index.html', views.logout_user, name='logout'),
    path('add-item-to-cart/<int:pk>', views.add_item_to_cart, name='add_item_to_cart'),
    path('delete_item/<int:pk>', views.CartDeleteItem.as_view(), name='cart_delete_item'),
    path('make-order/', views.make_order, name='make_order'),
]