from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views import View


def logout_view(requests: HttpRequest):
    logout(requests)
    return redirect(reverse("main:home_page"))


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
