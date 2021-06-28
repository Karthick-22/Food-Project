from django import urls
from django.urls import path
from . import views



urlpatterns=[
    path('',views.home,name='home'),
    path('feed_back',views.feed_back,name='feed_back'),
    path('login',views.login,name='login'),
    path('login_main',views.login_main,name='login_main'),
    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('adminlogin_page',views.adminlogin_page,name='adminlogin_page'),
    path('admin_main_login',views.admin_main_login,name='admin_main_login'),
    path('register_first',views.register_first,name='register_first'),
    path('register_db',views.register_db,name='register_db'),
    path('quality',views.quality,name='quality'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('forget',views.forget,name='forget'),
    path('products',views.products,name='products'),
    path('cart',views.cart,name='cart'),
    path('invoice',views.invoice,name='invoice'),
    path('normal',views.normal,name='normal'),
    path('inbox',views.inbox,name='inbox'),
    path('compose',views.compose,name='compose'),
    path('chat',views.chat,name='chat'),
    path('product_detail',views.product_detail,name='product_detail'),
    path('product_list',views.product_list,name='product_list'),
    path('product_list_page',views.product_list_page,name='product_list_page'),
    path('sub_category_list',views.sub_category_list,name='sub_category_list'),
    path('campaign_list',views.campaign_list,name='campaign_list'),
    path('campaign_button',views.campaign_button,name='campaign_button'),
    path('export_table',views.export_table,name='export_table'),
    path('view_mail',views.view_mail,name='view_mail'),
    path('mail_inbox',views.mail_inbox,name='mail_inbox'),
    path('basic_form_elements',views.basic_form_elements,name='basic_form_elements'),
    path('add_sub_category',views.add_sub_category,name='add_sub_category'),
    path("index",views.index,name="index"),
    path("form_examples",views.form_examples,name="form_examples"),
    path("edit/<int:id>",views.edit,name="edit"),
    path("user_update/<int:id>",views.user_update,name="user_update"),
    path("delete/<int:id>",views.delete,name="delete"),
    path("edit_offer/<int:id>",views.edit_offer,name="edit_offer"),
    path("user_update_offer/<int:id>",views.user_update_offer,name="user_update_offer"),
    path("delete_offer/<int:id>",views.delete_offer,name="delete_offer"),
    path("edit_sub/<int:id>",views.edit_sub,name="edit_sub"),
    path("user_update_sub/<int:id>",views.user_update_sub,name="user_update_sub"),
    path("delete_sub/<int:id>",views.delete_sub,name="delete_sub"),
    path('logout',views.logout,name='logout')
   
]

