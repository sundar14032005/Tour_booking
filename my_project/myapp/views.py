from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Tour, Booking


def home(request):
    tours = Tour.objects.all()
    return render(request, "home.html", {"tours": tours})


def reg(request):
    if request.method == "POST":
        User.objects.create_user(
            username=request.POST["username"],
            password=request.POST["password"]
        )
        return redirect("login")

    return render(request, "reg.html")


def login_user(request):
    if request.method == "POST":
        u = authenticate(
            username=request.POST["username"],
            password=request.POST["password"]
        )

        if u:
            login(request, u)
            return redirect("home")

    return render(request, "login.html")


def logout_user(request):
    logout(request)
    return redirect("login")


@login_required
def Book_tour(request, tour_id):

    tour = get_object_or_404(Tour, id=tour_id)

    if request.method == "POST":
        seats = int(request.POST["seats"])

        if seats <= tour.available_seats:
            Booking.objects.create(
                user=request.user,
                tour=tour,
                seats=seats
            )

            tour.available_seats = tour.available_seats - seats
            tour.save()

            return redirect("home")

    return render(request, "book_tour.html", {"tour": tour})