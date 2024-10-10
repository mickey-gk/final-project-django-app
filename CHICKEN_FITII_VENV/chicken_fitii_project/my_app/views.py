from django.shortcuts import render

# navigation bar
def navigation_items():
    return [
        {'name':'Home', 'url':'index'},
        {'name':'products', 'url': 'products'},
        {'name':'Log in', 'url':'login'},
        {'name':'Sign in', 'url':'register'},
        {'name':'About', 'url':'about'},
    ]

def image_links():
    return [
        { 'url': 'images/chicken_01.png'},
        {'url': 'images/chicken_02.png'},
        {'url':'images/chicken_03.png'},
        {'url':'images/chicken_04.png'}
    ]

# Creating views here.
def index(request):
    nav_items = navigation_items()
    images_links = image_links()  # Get the image links
    return render(request, 'index.html', {
        'nav_items': nav_items,
        'images_links': images_links,  # Pass the images to the template
    })

def login(request):
    nav_items = navigation_items()
    return render(request, 'login.html', {'nav_items':nav_items})

def register(request):
    nav_items = navigation_items()
    return render(request, 'register.html', {'nav_items':nav_items})

def about(request):
    nav_items = navigation_items()
    return render(request, 'about.html', {'nav_items':nav_items})

def products(request):
    nav_items = navigation_items()
    return render(request, 'products.html', {'nav_items': nav_items})


