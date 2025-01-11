from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpRequest
from django.shortcuts import render, reverse, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django.views.generic.detail import DetailView
from .models import Receipt


# Create your views here.

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
        self.object.save()
        url = reverse("main:home_page")
        return redirect(url)


class UpdateReceiptView(UpdateView):
    model = Receipt
    fields = "name", "description", "cooking_steps", "image", "author", "cooking_time"
    success_url = reverse_lazy("main:receipt_details")

    def get_success_url(self):
        return reverse("main:receipt_details", kwargs={"pk": self.object.pk})

    def is_valid(self):
        self.save()
        url = reverse("main:home_page")
        image = self.cleaned_data['image']
        fs = FileSystemStorage()
        fs.save(image.name, image)
        return redirect(url)

