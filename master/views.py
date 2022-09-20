from django.shortcuts import render
from django.views import generic as views
from re import template
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings

from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin

from user.forms import UserRegistrationForm
from master.forms import FeedbackForm



def home_view(request):
    template_name = 'master/home.html'
    return render(request,template_name)

    
class HomeView(views.TemplateView):
    template_name = "master/home.html"

# class CategoryView(views.TemplateView):
    # template_name="master/category.html"

class OrderView(views.TemplateView):
    template_name="master/order.html"

class ContactView(views.TemplateView):
    template_name="master/contact.html"

class AboutUsView(views.TemplateView):
    template_name="master/aboutus.html"


    

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



#     # forgot password----


# class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
#     template_name = 'master/password_reset.html'
#     email_template_name = 'master/password_reset_email.html'
#     success_message = "We've emailed you instructions for setting your password, " \
#                       "if an account exists with the email you entered. You should receive them shortly." \
#                       " If you don't receive an email, " \
#                       "please make sure you've entered the address you registered with, and check your spam folder."
#     success_url = reverse_lazy('master:home')
    
    


