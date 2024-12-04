from django.urls import path
from webapp import views
urlpatterns=[
    path('home/',views.home,name='home'),
    path('product_page/', views.product_page, name='product_page'),
    path('about_page/', views.about_page, name='about_page'),
    path('contact_page/', views.contact_page, name='contact_page'),
    path('save_page/', views.save_page, name='save_page'),
    path('product_filtered/<cat_name>/', views.product_filtered, name='product_filtered'),
    path('product_single/<int:pro_id>/', views.product_single, name='product_single'),
    path('signup_page',views.signup_page,name='signup_page'),
    path('', views.signin_page, name='signin_page'),
    path('save_signup/',views.save_signup,name='save_signup'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),

    path('save_cart/', views.save_cart, name='save_cart'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('save_order/', views.save_order, name='save_order'),
    path('payment/',views.payment,name='payment'),

    path('delete_cart/<int:cart_id>/', views.delete_cart, name='delete_cart'),

]