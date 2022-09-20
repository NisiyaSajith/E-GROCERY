from django import forms
from product.models import Product


#  create/update from course
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "category",
                  "unit", "stock", "available", "image", ]
