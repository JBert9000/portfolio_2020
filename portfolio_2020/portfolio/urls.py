from django.urls import path
from . import views
from .views import sendEmail, successView

urlpatterns = [
    path('', views.home, name="portfolio-home"),
    path('home/', sendEmail, name="portfolio-send-mail"),
    path('home/', successView, name="portfolio-success"),
]
