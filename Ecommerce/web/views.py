from django.shortcuts import render
from . models import Product, Testimonial, Contact
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

# Create your views here.
def index(request):
    context = {
        'produ': Product.objects.all(),
        'testu': Testimonial.objects.all()
    }

    if request.method=="POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact1 = Contact(
            name = name,
            phone = phone,
            email = email,
            message = message
        )

        contact1.save()
    return render(request, 'web/index.html', context)

def about(request):
    return render(request, 'web/about.html')

def chocolate(request):
    context = {
        'produ': Product.objects.all()
    }
    return render(request, 'web/chocolate.html', context)

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact1 = Contact(
            name = name,
            phone = phone,
            email = email,
            message = message
        )

        contact1.save()
    return render(request, 'web/contact.html')

def testimonial(request):
    context = {
        'testu': Testimonial.objects.all()
    }
    return render(request, 'web/testimonial.html', context)

def login1(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('signup')

    return render(request, "web/login.html")

def signup(request):
    if request.method=="POST":
        username = request.POST.get('username')
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if pass1 == pass2:
            user = User.objects.create_user(username, email, pass1)
            user.first_name = f_name
            user.last_name = l_name
            user.save()
    return render(request, "web/signup.html")

def logout1(request):
    logout(request)
    return redirect('index')