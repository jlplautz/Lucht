from django.urls import path

from srcprg.freight import views as v

app_name = 'freight'

urlpatterns = [
    path('', v.FreightListView.as_view(), name='freight_list'),
    path('create/', v.FreightCreateView.as_view(), name='freight_create'),
]
