from django.shortcuts import render

def index(request):
    return render(request, "_Blog/index.html", {})