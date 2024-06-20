from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import BrandsForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@method_decorator(login_required(login_url=reverse_lazy("home")), name="dispatch")
class Brands(FormView):
    form_class = BrandsForm
    template_name = "brands.html"
    success_url = reverse_lazy("home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Add a new Brand'
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)