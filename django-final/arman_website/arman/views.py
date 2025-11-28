from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product


def home(request):
    # Redirect unauthenticated users to register page
    if not request.user.is_authenticated:
        return redirect('register')
    
    context = {
        'title': 'Arman Website',
        'welcome_text': 'Welcome to Arman\'s Django Template Demo!'
    }
    return render(request, 'arman/home.html', context)


def products(request):
    items = Product.objects.all()
    context = {
        'title': 'Products',
        'welcome_text': 'Explore our product list rendered via Django templates.',
        'products': items
    }
    return render(request, 'arman/products.html', context)


def product_detail(request, pk):
    item = get_object_or_404(Product, pk=pk)
    return render(request, 'arman/product_detail.html', {'product': item})
