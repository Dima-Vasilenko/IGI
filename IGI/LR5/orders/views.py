from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from django.contrib.auth.decorators import login_required

from django.utils import timezone
from django.db.models import Avg, Max, Count

from statistics import median

from .models import Order

from .forms import OrderForm

import datetime

import calendar

from zoneinfo import ZoneInfo

import logging

logger = logging.getLogger(__name__)

import matplotlib

matplotlib.use('Agg')

import matplotlib.pyplot as plt

import os


@login_required
def order_list(request):

    orders = Order.objects.all()

    if not request.user.is_superuser:

        try:

            client_profile = request.user.clientprofile

            orders = orders.filter(
                client=client_profile
            )

        except:

            pass

    return render(request, 'orders/order_list.html', {
        'orders': orders
    })


@login_required
def order_create(request):

    if request.method == 'POST':

        form = OrderForm(request.POST)

        if form.is_valid():

            form.save()

            logger.info(
                f"Создан заказ пользователем {request.user}"
            )

            return redirect('/orders/')

    else:

        form = OrderForm()

    return render(request, 'orders/order_form.html', {
        'form': form
    })


@login_required
def order_update(request, pk):

    order = get_object_or_404(
        Order,
        pk=pk
    )

    if request.method == 'POST':

        form = OrderForm(
            request.POST,
            instance=order
        )

        if form.is_valid():

            form.save()

            logger.info(
                f"Обновлен заказ #{order.id}"
            )

            return redirect('/orders/')

    else:

        form = OrderForm(instance=order)

    return render(request, 'orders/order_form.html', {
        'form': form
    })


@login_required
def order_delete(request, pk):

    order = get_object_or_404(
        Order,
        pk=pk
    )

    if request.method == 'POST':

        logger.info(
            f"Удален заказ #{order.id}"
        )

        order.delete()

        return redirect('/orders/')

    return render(request, 'orders/order_delete.html', {
        'order': order
    })


def statistics_view(request):

    logger.info("Открыта статистика")

    orders = Order.objects.all()

    total_orders = orders.count()

    avg_price = orders.aggregate(
        Avg('price')
    )['price__avg']

    max_price = orders.aggregate(
        Max('price')
    )['price__max']

    prices = list(
        orders.values_list(
            'price',
            flat=True
        )
    )

    median_price = None

    if prices:

        median_price = median(prices)

    popular_cargo = (
        orders.values('cargo_type__name')
        .annotate(total=Count('id'))
        .order_by('-total')
        .first()
    )


    current_timezone = timezone.get_current_timezone()
    local_time = datetime.datetime.now(current_timezone)


    utc_time = datetime.datetime.now(
        datetime.timezone.utc
    )

    current_calendar = calendar.month(
        local_time.year,
        local_time.month
    )

    statuses = (
        orders.values('status')
        .annotate(total=Count('id'))
    )

    labels = [
        item['status']
        for item in statuses
    ]

    values = [
        item['total']
        for item in statuses
    ]

    plt.figure(figsize=(6, 4))

    plt.bar(labels, values)

    chart_dir = os.path.join(
        'media',
        'charts'
    )

    os.makedirs(
        chart_dir,
        exist_ok=True
    )

    chart_path = os.path.join(
        chart_dir,
        'orders_chart.png'
    )

    plt.savefig(chart_path)

    plt.close()

    return render(request, 'orders/statistics.html', {

        'total_orders': total_orders,

        'avg_price': avg_price,

        'max_price': max_price,

        'median_price': median_price,

        'popular_cargo': popular_cargo,

        'local_time': local_time,

        'utc_time': utc_time,

        'current_calendar': current_calendar,
    })