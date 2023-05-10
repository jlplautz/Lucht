from django.urls import path

from srcprg.truck import views as v

app_name = 'truck'

urlpatterns = [
    path('', v.TruckListView.as_view(), name='truck_list'),
    path('create/', v.TruckCreateView.as_view(), name='truck_create'),
]
