from django.shortcuts import render, get_object_or_404, redirect
from .models import about
from .forms import ProductAboutForm

# Create your views here.


def About(request):
    abouts = about.objects.all()
    return render(request, "about.html", {"abouts": abouts})


def edit_about(request, pk=None):
    """
    Create a view that allows us to create
    or edit a post depending if the Post ID
    is null or not
    """
    from .models import about
    about = get_object_or_404(about, pk=pk) if pk else None
    
    if request.method == "POST":
        form = ProductAboutForm(request.POST, request.FILES, instance=about)
        if form.is_valid():
            about = form.save()
            return redirect(About)
    else:
        form = ProductAboutForm(instance=about)
    return render(request, 'about-form.html', {'form': form})
