from django.views.generic import TemplateView, View, UpdateView
from add_car.models import Car, UserCar
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from user_credintial.forms import ChangeUserData
from django.contrib.auth.models import User

# Create your views here.
@method_decorator(login_required(login_url=reverse_lazy("home")), name="dispatch")
class ProfileView(TemplateView):
    template_name = 'user_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_purchases'] = Car.objects.filter(usercar__user=self.request.user)
        print(context)
        return context

@method_decorator(login_required(login_url=reverse_lazy("home")), name="dispatch")
class DeleteProfilePost(View):
    success_url = reverse_lazy("profile")

    def post(self, request, **kwargs):
        car_id = kwargs['id']
        user_car = UserCar.objects.filter(user=request.user, car_id=car_id).first()
        if user_car:
            user_car.delete()
        return redirect(self.success_url)


@method_decorator(login_required(login_url=reverse_lazy("home")), name="dispatch")
class EditProfile(UpdateView):
    model = User
    form_class = ChangeUserData
    template_name = "change_profile.html"
    success_url = reverse_lazy("change_profile")

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, 'Account has been updated successfully')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = "Edit Profile"
        return context
