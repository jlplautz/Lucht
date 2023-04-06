from django.contrib.auth.views import LoginView, logout_then_login
from django.urls import path

from .views import dashboard, signup

app_name = 'authentication'

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('cadastro/', signup, name='signup'),
    path(
        'login/',
        LoginView.as_view(
            template_name='authentication/signin.html',
            redirect_authenticated_user=True,
        ),
        name='login',
    ),
    path('logout/', logout_then_login, name='logout'),
]
