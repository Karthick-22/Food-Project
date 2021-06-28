from django import forms
from . models import category_adding,offers,sub_cate

class Imageform(forms.ModelForm):
    name=forms.CharField(label='Category name')
    product=forms.CharField(label='Product name')
    title=forms.CharField(label='Title')
    campaign=forms.CharField(label='Campaign')
    category=forms.CharField(label='Category')
    sub_category=forms.CharField(label='Sub_category')


    class Meta:
        model=category_adding
        model=offers
        model=sub_cate

        fields="__all__"