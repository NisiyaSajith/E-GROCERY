from django.urls import path
from customer import views
app_name = "customer"


urlpatterns = [
    path("create/", views.CustomerCreateView.as_view(), name="create"),
    path("list/", views.CustomerListView.as_view(), name="list"),
]
