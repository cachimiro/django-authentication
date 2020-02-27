from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductPostForm

# Create your views here.


def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})


def create_or_edit_product(request, pk=None):
    """
    Create a view that allows us to create
    or edit a post depending if the Post ID
    is null or not
    """
    from .models import Product
    Product = get_object_or_404(Product, pk=pk) if pk else None
    
    if request.method == "POST":
        form = ProductPostForm(request.POST, request.FILES, instance=Product)
        if form.is_valid():
            Product = form.save()
            return redirect(all_products)
    else:
        form = ProductPostForm(instance=Product)
    return render(request, 'productform.html', {'form': form})
