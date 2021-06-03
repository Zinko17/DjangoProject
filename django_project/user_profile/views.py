from django.contrib.auth.models import AnonymousUser
from django.utils import timezone

from django.http import HttpResponse
from django.shortcuts import render
from .models import Profile, Order
from .forms import OrderForm
from .services import incrementOrderCount, countMoney, time_check
from spa.models import Service


def profile_page(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except (Profile.DoesNotExist, TypeError):
        return HttpResponse('404')
    return render(request, 'profile.html', {'profile': profile})


def order_page(request, service_id):
    try:
        service = Service.objects.get(id=service_id)
    except Service.DoesNotExist:
        return HttpResponse(404)
    user = request.user
    form = OrderForm(initial={'user': user, 'service': service})
    if request.method == "POST":
        form = OrderForm(request.POST, initial={'user': user, 'service': service})
        if form.is_valid():
            incrementOrderCount(user.profile)
            countMoney(user.profile, form.instance)
            form.save()
    return render(request, 'order.html', {'form': form,'service':service})


def my_orders(request):
    user = request.user
    if isinstance(user, AnonymousUser):
        return HttpResponse('Please login!')
    orders = Order.objects.filter(user=user)
    return render(request, 'my_order.html', {'orders': orders})


def delete_order(request, order_id):
    try:
        order = Order.objects.get(user=request.user, id=order_id)
    except Order.DoesNotExist:
        return HttpResponse('?')
    if request.method == 'POST':
        order_date = order.date_created
        if time_check(order_date):
            order.delete()
        else:
            return HttpResponse('Time is Up!')
    return render(request, 'delete_order.html')


def update_order(request, order_id):
    try:
        order = Order.objects.get(user=request.user, id=order_id)
    except Order.DoesNotExist:
        return HttpResponse('?')
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            if time_check(order.date_created):
                form.save()
            else:
                return HttpResponse('Time is UP!')
    return render(request, 'order.html', {'form': form})
