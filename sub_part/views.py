from django.http import request
from django.shortcuts import render
from . models import feedback,register,adminpage,category_adding,add_cate,offers,sub_cate
import easygui
from . forms import Imageform
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from sub_part.models import category_adding
from django.contrib.auth import logout as log

# Create your views here.
def home(request):

    return render(request,'home.html')


def feed_back(request):
    if request.method=="POST":
        feed_display=feedback(email_id=request.POST['email_id'],
                              feedback_text=request.POST['feedback_text']
                              )
        feed_display.save()
        easygui.msgbox("your data has been stored successfully",title='Feedback Form')
        return redirect(home)
    return render(request,'home.html')

def login(request):
    return render(request,'login.html')
def register_first(request):
    return render(request,'register.html')
def login_main(request):
    if request.method=='POST':
        if register.objects.filter(user_name=request.POST['user_name'],password=request.POST['password']).exists():
            ex2=register.objects.get(user_name=request.POST['user_name'],password=request.POST['password'])
            easygui.msgbox("logged successfully!",title="Login form")
            return render(request,'login.html',{'ex2':ex2})
        else:
            
            context={'msg':'you entered wrong username and password'}
            easygui.msgbox("wrong username and password!",title="Login form")
            return render(request,'login.html',context)

    return render(request,'login.html')
def register_db(request):
    if request.method=="POST":
        reg_display=register(first_name=request.POST['first_name'],
                               last_name=request.POST['last_name'],
                                user_name=request.POST['user_name'],
                                password=request.POST['password'],
                                phone_no=request.POST['phone_no']
                               )
        reg_display.save()
        easygui.msgbox("your data has been stored successfully",title="Admin Form")
        return redirect(login)
    return render(request,'register.html')
def quality(request):
    return render(request,'quality.html')
def adminlogin(request):
    return render(request,'adminlogin.html')
def admin_main_login(request):
    if request.method=='POST':
        if adminpage.objects.filter(admin_email=request.POST['admin_email'],admin_password=request.POST['admin_password']).exists():
            ex1=adminpage.objects.get(admin_email=request.POST['admin_email'],admin_password=request.POST['admin_password'])
            easygui.msgbox("logged successfully!",title="Login form")
            return render(request,'dashboard.html',{'ex1':ex1})
        else:
            
            context={'msg':'you entered wrong username and password'}
            easygui.msgbox("wrong username and password!",title="Login form")
            return render(request,'adminlogin.html',context)

    return render(request,'adminlogin.html')
def adminlogin_page(request):
    if request.method=="POST":
        admin_display=adminpage(admin_name=request.POST['admin_name'],
                                admin_email=request.POST['admin_email'],
                               admin_password=request.POST['admin_password']
                                
                              )
        admin_display.save()
        easygui.msgbox("your data has been stored successfully",title="Admin Form")
        return redirect(adminlogin)
    return render(request,'adminlogin.html')
@login_required(login_url='login')
def dashboard(request):
    var1=register.objects.get('first_name')
    return render(request,'dashboard.html',{'var1':var1})
    return render(request,'dashboard.html')
def forget(request):
    return render(request,'forget.html')
def products(request):
    return render(request,'products.html')
def cart(request):
    return render(request,'cart.html')
def invoice(request):
    return render(request,'invoice.html')
def normal(request):
    return render(request,'normal.html')   
def inbox(request):
    return render(request,'inbox.html')
def compose(request):
    return render(request,'compose.html')
def chat(request):
    return render(request,'chat.html')
def product_detail(request):
    return render(request,'product_detail.html')
def product_list(request):
    var1 = add_cate.objects.all()
    context={
        'var1':var1
    }
    return render(request,'product_list.html',context)
def product_list_page(request):
    return render(request,'product_list_page.html')
def sub_category_list(request):
    var3 = sub_cate.objects.all()
    context={
        'var3': var3
    }
    return render(request,'sub_category_list.html',context)
def campaign_list(request):
    var2 = offers.objects.all()
    context={
        'var2':var2
    }
    return render(request,'campaign_list.html',context)

def export_table(request):
    return render(request,'export_table.html')
def view_mail(request):
    return render(request,'view_mail.html')
# def add_sub_category(request):
#     return render(request,'add_sub_category.html')
def mail_inbox(request):
    return render(request,'mail_indox.html')


def index(request):
   form=Imageform()
   return render(request,'index.html',{'form':form})
       
    
def form_examples(request):
    return render(request,'form_examples.html')


def basic_form_elements(request):
    if request.method=='POST':
        var1=add_cate()
        var1.category_name=request.POST.get('cate_name')
        var1.product_name=request.POST.get('pro_name')
        if len(request.FILES) != 0:
            var1.image_file=request.FILES['file_image']
        var1.stock_name=request.POST.get('selectstock')
        var1.save()
        easygui.msgbox("your data has been stored successfully",title="Admin Form")
        return redirect( product_list)
    return render(request,'basic_form_elements.html')

def edit(request,id):
    var1 =add_cate.objects.get(id=id)
    context={'var1':var1}

     
    
    return render(request,'edit.html',context)   

def user_update(request,id):
    var1 =add_cate(id=id)
    var1.category_name=request.POST.get('cate_name')
    var1.product_name=request.POST.get('pro_name')
    if len(request.FILES) != 0:
        var1.image_file=request.FILES['file_image']
    var1.stock_name=request.POST.get('selectstock')
    var1.save()
    easygui.msgbox("your data has been updated successfully",title="Admin Form")
    return redirect(product_list)

def delete(request,id):
    var1=add_cate.objects.get(id=id)
    var1.delete()
    easygui.msgbox("your data has been deleted",title="Admin Form")
    return redirect(product_list)

def logout(request):
    log(request)
    easygui.msgbox("logged out")
    return render(request,'adminlogin.html')


def campaign_button(request):
    if request.method=='POST':
        var2=offers()
        var2.title=request.POST.get('title')
        var2.campaign=request.POST.get('campaign')
        if len(request.FILES) != 0:
            var2.image_file=request.FILES['file_image']
        var2.stock_name=request.POST.get('selectstock')
        var2.save()
        easygui.msgbox("your data has been stored successfully",title="Admin Form")
        return redirect( campaign_list)
    return render(request,'campaign_button.html')

def edit_offer(request,id):
    var2 =offers.objects.get(id=id)
    context={'var2':var2}

     
    
    return render(request,'edit_offer.html',context)   

def user_update_offer(request,id):
    var2 =offers(id=id)
    var2.title=request.POST.get('title')
    var2.campaign=request.POST.get('campaign')
    if len(request.FILES) != 0:
        var2.image_file=request.FILES['file_image']
    var2.stock_name=request.POST.get('selectstock')
    var2.save()
    easygui.msgbox("your data has been updated successfully",title="Admin Form")
    return redirect(campaign_list)

def delete_offer(request,id):
    
    var2=offers.objects.get(id=id)
    var2.delete()
    easygui.msgbox("your data has been deleted",title="Admin Form")
    return redirect(campaign_list)


def add_sub_category(request):
    if request.method=='POST':
        var3=sub_cate()
        var3.category=request.POST.get('category')
        var3.sub_category=request.POST.get('sub_category')
        if len(request.FILES) != 0:
            var3.image_file=request.FILES['file_image']
        var3.stock_name=request.POST.get('selectstock')
        var3.save()
        easygui.msgbox("your data has been stored successfully",title="Admin Form")
        return redirect( sub_category_list)
    return render(request,'add_sub_category.html')

def edit_sub(request,id):
    var3=sub_cate.objects.get(id=id)
    context={'var3':var3}

    return render(request,'edit_sub.html',context)   

def user_update_sub(request,id):
    var3=sub_cate(id=id)
    var3.category=request.POST.get('category')
    var3.sub_category=request.POST.get('sub_category')
    if len(request.FILES) != 0:
        var3.image_file=request.FILES['file_image']
    var3.stock_name=request.POST.get('selectstock')
    var3.save()
    easygui.msgbox("your data has been updated successfully",title="Admin Form")
    return redirect(sub_category_list)

def delete_sub(request,id):
    var3=sub_cate.objects.get(id=id)
    var3.delete()
    easygui.msgbox("your data has been deleted",title="Admin Form")
    return redirect(sub_category_list)