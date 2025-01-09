from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView


def logout_view(requests: HttpRequest):
    logout(requests)
    return redirect(reverse("main:home_page"))


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "auth/registration.html"
    success_url = reverse_lazy("main:home_page")

    def form_valid(self, form):
        response = super().form_valid(form)

        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        user = authenticate(self.request, username=username, password=password)
        login(request=self.request, user=user)
        return response



# def authenticate_view(request: HttpRequest):
#     if request.method == "GET":
#         if request.user.is_authenticated:
#             return redirect("main:create_receipt")
#
#         return render(request, "auth/authorization.html")
#
#     username = request.POST['login']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         return redirect("/main/")
