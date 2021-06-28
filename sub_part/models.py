from django.db import models

# Create your models here
class feedback(models.Model):
    email_id=models.EmailField()
    feedback_text=models.CharField(max_length=200)

    def __str__(self):
        return self.email_id

class register(models.Model):
    
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    user_name=models.EmailField()
    password=models.CharField(max_length=50)
    phone_no=models.CharField(max_length=15)

    def __str__(self):
        return self.user_name

class adminpage(models.Model):
    admin_name=models.CharField(max_length=50)
    admin_email=models.EmailField()
    admin_password=models.CharField(max_length=50)

    def __str__(self):
        return self.admin_name


class categoryadd(models.Model):
    name=models.CharField(max_length=100)
    product=models.CharField(max_length=100)
    image=models.ImageField(upload_to="picture/")
   
COLOR_CHOICES = (
    ('green','Stock'),
    ('blue', 'out of stock'),
   
)
class category_adding(models.Model):
    name=models.CharField(max_length=100)
    product=models.CharField(max_length=100)
    image=models.ImageField(upload_to="picture")
    stock =models.CharField(max_length=6, choices=COLOR_CHOICES, default='green')
  
class add_cate(models.Model):
    category_name=models.CharField(max_length=100)
    product_name=models.CharField(max_length=100)
    image_file=models.ImageField(upload_to="img",null=True,blank=True)
    stock_name=models.CharField(max_length=100)

    def __str__(self):
        return self.category_name
  
class offers(models.Model):
    title=models.CharField(max_length=100)
    campaign=models.CharField(max_length=100)
    image_field=models.ImageField(upload_to="imgoffer",null=True,blank=True)
    stock_name=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class sub_cate(models.Model):
    category=models.CharField(max_length=100)
    sub_category=models.CharField(max_length=100)
    image_field=models.ImageField(upload_to="imgsub",null=True,blank=True)
    stock_name=models.CharField(max_length=100)
    def __str__(self):
        return self.category