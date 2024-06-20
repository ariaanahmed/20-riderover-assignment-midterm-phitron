from django.urls import path
from .views import Brands

urlpatterns = [
    path("", Brands.as_view(), name="brands"),
]