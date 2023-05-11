from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .forms import FreightForm
from .models import Freight


class FreightListView(ListView):
    model = Freight
    paginator_by = 2


class FreightCreateView(CreateView):
    model = Freight
    form_class = FreightForm
    success_url = reverse_lazy('freight:freight_list')
