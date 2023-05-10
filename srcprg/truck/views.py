from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .forms import TruckForm
from .models import Truck


class TruckListView(ListView):
    model = Truck
    paginator_by = 2


class TruckCreateView(CreateView):
    model = Truck
    form_class = TruckForm
    success_url = reverse_lazy('truck:truck_list')
