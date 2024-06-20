from django.urls import path
from . import views
from .views import BuyCarView

urlpatterns = [
    path("", views.Add_car.as_view(), name="addcar"),
    path("car_detail/<int:id>/", views.Car_detail.as_view(), name="car_detail"),
    path('buycar/<int:id>/', BuyCarView.as_view(), name='buy_car'),
]

