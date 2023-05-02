from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .forms import DriverForm
from .models import Driver


class DriverListView(ListView):
    model = Driver
    paginator_by = 2


class DriverCreateView(CreateView):
    model = Driver
    form_class = DriverForm
    success_url = reverse_lazy('driver:driver_list')
