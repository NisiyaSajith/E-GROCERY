from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views import generic as views


from product.models import Product,Category,Unit
from product.forms import ProductForm

from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin

from user.forms import UserRegistrationForm
from master.forms import FeedbackForm

# product creation
class ProductCreateView(views.View):
    template_name = "product/form.html"
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("product:list")
    extra_context = {"action": "Create"}

    def get(self, request):
        context = {"form": self.form_class()}
        context.update(self.extra_context)
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)

    def form_invalid(self, form):
        context = {"form": form}
        context.update(self.extra_context)
        return render(self.request, self.template_name, context)



# # product listing
class ProductListView(views.ListView):
    template_name = "product/list.html"
    model = Product
    context_object_name = "products"

    
    def get_queryset(self):
        qs = self.model.objects.filter(status=True)
        return qs


# product detailing

class ProductDetailView(views.DetailView):
    template_name = 'product/detail.html'
    model = Product
    context_object_name = "product"
     # here we give context name only "course"because only if we click a course ,detail about that course is only available.this is for that purpose

    def get_queryset(self):
         qs = Product.objects.filter(status=True)
         return qs




# product updation
class ProductUpdateView(views.UpdateView):
     template_name = 'product/form.html'
     model = Product
     form_class = ProductForm
     success_url = reverse_lazy("product:list")
     extra_context = {"action": "Update"}


# delete course

class ProductDeleteView(views.DeleteView):
    template_name = 'product/delete.html'
    model = Product
    success_url = reverse_lazy("product:list")
    extra_context = {"action": "Delete",
                      "info": "Are you sure want to delete?"}

    def form_valid(self, form):
         self.object.status = False
         self.object.save()
         url = super().get_success_url()
         return redirect(url)



# class FeedbackView(views.FormView):
#     template_name = "master/feedback.html"
#     form_class = FeedbackForm
#     success_url = reverse_lazy("master:home")

#     def form_valid(self, form):
#         data = form.cleaned_data
#         subject = "Thank you for your valuable feedback!"
#         message = f"""
#         Hi {data.get("name")},

#         This is an auto generated mail. We will reach you soon.

#         Thanks and Regards,
#         Learning Team
#         """
#         from_email = settings.EMAIL_HOST_USER
#         to_email = [
#             data.get("email"),
#         ]
#         send_mail(subject=subject, message=message, from_email=from_email, recipient_list=to_email)
#         return super().form_valid(form)



# # email

# class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
#     template_name = 'master/password_reset.html'
#     email_template_name = 'master/password_reset_email.html'
#     success_message = "We've emailed you instructions for setting your password, " \
#                       "if an account exists with the email you entered. You should receive them shortly." \
#                       " If you don't receive an email, " \
#                       "please make sure you've entered the address you registered with, and check your spam folder."
#     success_url = reverse_lazy('master:home')
