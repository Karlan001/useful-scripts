from django.conf import settings
import logging

from django.core.exceptions import ValidationError
from django.core.files.storage import FileSystemStorage
from django.http import HttpRequest
from django.shortcuts import render, reverse, redirect
from django.template.defaultfilters import filesizeformat
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView
from django.views.generic.detail import DetailView
from .models import Receipt
from reciepts.settings import MAX_UPLOAD_SIZE

# Create your views here.

logger = logging.getLogger(__name__)


class HomePageView(ListView):
    template_name = "main/main.html"
    queryset = Receipt.objects.order_by("?")[:5]
    # model = Receipt
    context_object_name = "receipts"


class ProfilePageView(ListView):

    def get(self, request: HttpRequest):
        context = {
            "profile_receipt": Receipt.objects.filter(user_created_id=self.request.user.id).all()
        }
        return render(request, "main/profile-receipts-list.html", context=context)


class DetailReceiptDetailsView(DetailView):
    template_name = "main/receipt-details.html"
    model = Receipt
    context_object_name = "receipts"


class CreateReceiptView(CreateView):
    model = Receipt
    fields = "name", "description", "cooking_steps", "image", "author", "cooking_time"
    success_url = reverse_lazy("main:home_page")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user_created_id = self.request.user.id
        url = reverse("main:home_page")
        image = form.cleaned_data['image']
        fs = FileSystemStorage()
        if image:
            image_size = image.size
            if image_size >= MAX_UPLOAD_SIZE:
                return redirect("main:error")
            else:
                fs.save(image.name, image)
                self.object.save()
                return redirect(url)
        self.object.save()
        return redirect(url)


class UpdateReceiptView(UpdateView):
    model = Receipt
    fields = "name", "description", "cooking_steps", "image", "author", "cooking_time"
    success_url = reverse_lazy("main:receipt_details")
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse("main:receipt_details", kwargs={"pk": self.object.pk})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        url = reverse("main:home_page")
        image = form.cleaned_data['image']
        fs = FileSystemStorage()
        if image:
            image_size = image.size
            if image_size < MAX_UPLOAD_SIZE:
                fs.save(image.name, image)
                self.object.save()
                logger.info("Файл сохранен")
                return redirect(url)
            else:
                return redirect("main:error")
        return redirect(url)


def error_view(requests: HttpRequest):
    return render(requests, "main/exceptions-error.html")
