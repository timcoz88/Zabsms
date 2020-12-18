from django.shortcuts import render


# Create your views here.
def showDemoPage(request):
    return render(request, "demo.html")


def showLoginPage(request):
    return render(request, "login.html")
