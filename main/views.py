from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpRequest
from django.shortcuts import render, reverse, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django.views.generic.detail import DetailView, View
from .models import Receipt
from .forms import CreateReceiptForm


# Create your views here.

# def main(request: HttpRequest): Пока не используется
#     recipes = ['Плов', 'Рыба', 'Шаурма']
#     context = {
#         'product': recipes,
#     }
#     return render(request, 'main/index.html', context=context)

class HomePageView(ListView):
    template_name = "main/main.html"
    queryset = Receipt.objects.order_by("?")[:5]
    # model = Receipt
    context_object_name = "receipts"


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
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse("main:receipt_details", kwargs={"pk": self.object.pk})

    def is_valid(self, form):
        self.save()
        url = reverse("main:home_page")
        image = self.cleaned_data['image']
        fs = FileSystemStorage()
        fs.save(image.name, image)
        return redirect(url)

# def create_receipt(requests: HttpRequest):
#     if requests.method == "POST":
#         form = CreateReceiptForm(requests.POST, requests.FILES)
#         if form.is_valid():
#             form.save()
#             url = reverse("main:home_page")
#             image = form.cleaned_data['image']
#             fs = FileSystemStorage()
#             fs.save(image.name, image)
#             return redirect(url)
#     else:
#         form = CreateReceiptForm()
#     context = {
#         "form": form,
#     }
#     return render(requests, "main/create-receipt.html", context=context)

