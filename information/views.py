from django.shortcuts import render

# Create your views here.
def info(request):
    """A view that displays the information page"""
    return render(request, "info.html")
