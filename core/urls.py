from django.urls import path

from core import views

urlpatterns = [
    path('demo', views.showDemoPage, name="demo_page"),
    path('', views.showLoginPage, name="login_page")
]