from django.shortcuts import render
from django.views.generic import ListView, CreateView
from add_car.models import Car
from brands.models import Brands


# Create your views here.
def home(request):
    return render(request, "home.html")


# def car_list(request, brand_slug=None):
#     cars = Car.objects.all()
#     if brand_slug is not None:
#         brands = Brands.objects.get(slug=brand_slug)
#         cars = Car.objects.filter(brands=brands)
#         print(cars)
#     brands = Brands.objects.all()
#     return render(request, "home.html", {"cars": cars, "brands": brands})


class Car_list(ListView):
    template_name = 'home.html'
    context_object_name = 'cars'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cars'] = Car.objects.all()
        context['brands'] = Brands.objects.all()
        # print(context)
        return context

    def get_queryset(self):
        return Car.objects.all()



