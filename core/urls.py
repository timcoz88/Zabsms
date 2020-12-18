from django.urls import path

from core import views

urlpatterns = [
    path('', views.showDemoPage, name="demo_page")
]