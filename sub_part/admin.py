from django.contrib import admin
from . models import feedback,register,adminpage,categoryadd,category_adding,add_cate,offers,sub_cate
# Register your models here.
admin.site.register(feedback)
admin.site.register(register)
admin.site.register(adminpage)
admin.site.register(categoryadd)
admin.site.register(category_adding)
admin.site.register(add_cate)
admin.site.register(offers)
admin.site.register(sub_cate)