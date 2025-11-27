from django.shortcuts import render, redirect


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
    context = {
        'title': 'Products',
        'welcome_text': 'Explore our product list rendered via Django templates.'
    }
    return render(request, 'arman/products.html', context)
