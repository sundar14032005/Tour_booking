from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("reg/", views.reg, name="reg"),
    path("", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("book_tour/<int:tour_id>/", views.Book_tour, name="book_tour"),
]