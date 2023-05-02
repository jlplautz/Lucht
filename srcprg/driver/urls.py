from django.urls import path

from srcprg.driver import views as v

app_name = 'driver'

urlpatterns = [
    path('', v.DriverListView.as_view(), name='driver_list'),
    path('create/', v.DriverCreateView.as_view(), name='driver_create'),
]
