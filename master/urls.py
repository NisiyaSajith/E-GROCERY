from django.urls import path
from master import views
app_name = "master"


urlpatterns =[
    path("", views.HomeView.as_view(),name="home"),
    # path("category/",views.CategoryView.as_view(),name="category"),
    path("order/", views.OrderView.as_view(), name="order"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("aboutus/",views.AboutUsView.as_view(),name="aboutus"),
    # path("feedback/",views.FeedbackView.as_view(),name="feedback"),
    
]