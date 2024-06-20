from django.views.generic import CreateView, DetailView, View
from .forms import Car, CarForm, CommentForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from .models import UserCar, Car

@method_decorator(login_required(login_url=reverse_lazy("home")), name="dispatch")
class Add_car(CreateView):
    template_name = 'add_car.html'
    model = Car
    form_class = CarForm

    def get_success_url(self):
        return reverse_lazy("addcar")
    
    def form_valid(self, form):
        messages.success(self.request, "Car Added Successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Some error occurred")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = "Add Car"
        return context

class Car_detail(DetailView):
    model = Car
    pk_url_kwarg = 'id'
    template_name = 'car_detail.html'

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object  # post model object
        comments = post.comments.all()
        comment_form = CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        context["type"] = "Comments"
        return context

class BuyCarView(View):
    def post(self, request, id):
        car = get_object_or_404(Car, pk=id)
        if car.quantity > 0:
            car.quantity -= 1
            car.save()
            UserCar.objects.create(user=request.user, car=car)
            messages.success(request, "Car purchased successfully!")
        else:
            messages.error(request, "This car is out of stock.")
        return redirect('car_detail', id=id)
