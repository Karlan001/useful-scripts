from django.contrib.auth.views import LoginView
from django.urls import path, include
from .views import logout_view, RegisterView


app_name = 'authentication'

urlpatterns = [
    path('login/',
         LoginView.as_view(template_name="auth/authorization.html",
                           redirect_authenticated_user=True),
         name='login'),
    path('registration/', RegisterView.as_view(), name="registration"),
    path('logout/', logout_view, name='logout')
]

