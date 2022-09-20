from django import forms
from customer.models import Customer



#  create/update from course
class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=["user"]