from django.shortcuts import render, redirect, reverse
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

# Tugas 2 - main
@login_required(login_url='/login') # from tugas 4 - auth
def show_main(request):
    product_list = Product.objects.filter(user=request.user) # filter from tugas 4 - auth
    
    context = {
        'shop_name' : 'Station Eleven',
        'student_name' : 'Arya Raditya Kusuma',
        'class' : 'PBP F',
        'user_name': request.user.username, # from tugas 4 - auth
        'product_list': product_list, # from tugas 3 - forms
        'last_login': request.COOKIES['last_login'], # from tugas 4 - auth
    }

    return render(request, "main.html", context)

# Tugas 3 - forms, xml, json
def create_product_list(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_list = form.save(commit=False) # from tugas 4 - auth
        product_list.user = request.user # from tugas 4 - auth
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_list.html", context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# Tugas 4 - auth
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

# tugas 5 - add/edit
def edit_product(request, id):
    mood = Product.objects.get(pk = id)
    form = ProductForm(request.POST or None, instance=mood)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = Product.objects.get(pk = id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))