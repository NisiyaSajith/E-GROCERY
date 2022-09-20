from django.shortcuts import render,redirect
from django.views import generic as views
from customer.models import Customer 
from django.urls import reverse_lazy
from customer.forms import CustomerForm

from user.forms import UserRegistrationForm


# simple view
class CustomerCreateView(views.View):
    template_name= 'customer/form.html'
    model = Customer
    form_class=UserRegistrationForm
    success_url=reverse_lazy("login")
    extra_context={"action":"Create"}

    def get(self,request):
        context={
            "form":self.form_class
        }
        context.update(self.extra_context)
        return render(request,self.template_name,context)

    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)

    def form_valid(self,form):
            data=form.cleaned_data
            form.instance.username=data["email"]
            user=form.save()
            customer=Customer.objects.create(user=user)
            return redirect(self.success_url)

    def form_invalid(self,form):
            context = {"form": form}
            context.update(self.extra_context)
            return render(self.request,self.template_name,context)


    
# customer list view
class CustomerListView(views.ListView):
    template_name = 'customer/list.html'
    model = Customer
    context_object_name = "customers"

    def get_queryset(self):
        qs=Customer.objects.filter(status=True)
        return qs
