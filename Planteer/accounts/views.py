from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,logout, authenticate
from django.contrib import messages


# Create your views here.

def sign_up(request: HttpRequest):

    if request.method =="POST":

        try:
            new_user = User.objects.create_user(
                username = request.POST["username"],
                password = request.POST["password"],
                email = request.POST["email"],
                first_name = request.POST["first_name"],
                last_name = request.POST["last_name"]
                )
            new_user.save()
            # messages.success(request, "Registered User Successfuly", "alart-success")
            return redirect("accounts:sign_in")
        except Exception as e:
            print(e)


    return render(request, "accounts/signup.html")

def sign_in(request: HttpRequest):

    if request.method == "POST":

        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])

        if user:
            login(request, user)
            # messages.success(request, "Logged in successfuly", "alert-success")
            return redirect(request.GET.get("next","/"))
        # else:
            # messages.error(request, "Please try agian. your credential are wrong", "alert-danger")
            


    return render(request, "accounts/signin.html")

def log_out(request: HttpRequest):

    logout(request)
    # messages.success(request, "loged out Successfuly","alert-warning")

    return redirect(request.GET.get("next","/"))