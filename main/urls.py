from django.conf.urls.static import static
from django.template.defaulttags import url
from django.urls import path, include
from django.views.generic import RedirectView

from .views import (HomePageView,
                    UpdateReceiptView,
                    DetailReceiptDetailsView,
                    CreateReceiptView,
                    ProfilePageView,
                    error_view,)

app_name = 'main'

urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('profile/', ProfilePageView.as_view(), name='profile'),
    path("receipt_details/<int:pk>", DetailReceiptDetailsView.as_view(), name="receipt_details"),
    path('create-receipt/', CreateReceiptView.as_view(), name="create_receipt"),
    path('update-receipt/<int:pk>/update', UpdateReceiptView.as_view(), name="update_receipt"),
    path("error/", error_view, name="error"),
]

