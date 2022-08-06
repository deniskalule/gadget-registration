from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ItemForm, PersonForm, BadgeForm, BadgeFormOut
from .models import *


@login_required(login_url='login')
def home(request):
    # return HttpResponse("Hello Uganda, Am John Paul")
    items_results = Item.objects.all()
    badge_results = Badge.objects.all()
    person_results = Person.objects.all()
    items_count = items_results.count()
    badge_count = badge_results.count()
    person_count = person_results.count()
    context = {
        'items_results': items_results,
        'items_count': items_count,
        'badge_count': badge_count,
        'person_count': person_count,
    }
    return render(request, "home.html", context)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            print('Login Successful!')
            return redirect('home')
        else:
            messages.error(request, 'Username or Password not correct,Try again')
            return redirect('login')
    else:
        return render(request, 'login.html')


@login_required(login_url='home')
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        print('logged out from App..')
        return redirect('login')


# Creating, Validating and saving forms
@login_required(login_url='home')
def register_item(request):
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('badge')
    else:
        form = ItemForm()
    context = {
        "form_item": form
    }
    return render(request, 'register_item.html', context)


@login_required(login_url='home')
def person(request):
    form = PersonForm()
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('badge')
    else:
        form = PersonForm()
    context = {
        "form_person": form
    }
    return render(request, 'person.html', context)


@login_required(login_url='home')
def badge(request):
    form = BadgeForm()
    form_person = PersonForm()
    form_item = ItemForm()
    if request.method == 'POST':
        form = BadgeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BadgeForm()
    context = {
        "form_badge": form,
        "form_person": form_person,
        "form_item": form_item
    }
    return render(request, 'badge.html', context)


# Creating Functions to Update data by the Users
def update_person(request, pk):
    person = Person.objects.get(id=pk)
    form = PersonForm(instance=person)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'update_person.html', context)


def update_item(request, pk):
    item = Item.objects.get(id=pk)
    form = ItemForm(instance=item)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'update_person.html', context)


def update_badge(request, pk):
    badge = Badge.objects.get(id=pk)
    form = BadgeForm(instance=badge)
    if request.method == 'POST':

        form = BadgeForm(request.POST, instance=badge)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'update_badge.html', context)


def update_badge_out(request, pk):
    badge_out = Badge.objects.get(id=pk)
    form = BadgeFormOut(instance=badge_out)
    if request.method == 'POST':

        form = BadgeFormOut(request.POST, instance=badge_out)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'update_badge_out.html', context)


def view_items(request):
    items_results = Item.objects.all()
    items_count = items_results.count()
    context = {
        'items_results': items_results,
        'items_count': items_count
    }
    return render(request, 'view_items.html', context)


def view_badge(request):
    badge_results = Badge.objects.all()
    return render(request, 'view_badge.html', {'badge_results': badge_results})


def view_person(request):
    person_results = Person.objects.all()
    return render(request, 'view_person.html', {'person_results': person_results})


# function for deleting person
def delete_person(request, pk):
    person_delete = Person.objects.get(id=pk)
    person_delete.delete()
    return redirect('view_person')


# function for deleting item
def delete_item(request, pk):
    item_delete = Item.objects.get(id=pk)
    item_delete.delete()
    return redirect('view_item')


# function for deleting badge
def delete_badge(request, pk):
    badge_delete = Badge.objects.get(id=pk)
    badge_delete.delete()
    return redirect('view_badge')


# function to search in the data Person
def person_search_bar(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            persons = Person.objects.filter(organisation__icontains=query)
            return render(request, 'person_search.html', {'persons': persons})
        else:
            print("No person to search from")
            return render(request, 'person_search.html', {})


# function to search in the data item
def item_search_bar(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            items = Item.objects.filter(item_name__icontains = query)
            context = {
                'items': items
                       }
            return render(request, 'item_search.html', context)
        else:
            print("No Items to search from")
            return render(request, 'item_search.html', {})


# Function to search for badges or badged items
def badge_search_bar(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            badges = Badge.objects.filter(location__icontains=query)

            context = {
                'badges': badges,
            }
            return render(request, 'badge_search.html', context)
        else:
            print("No Badge to search from")
            return render(request, 'badge_search.html', {})
