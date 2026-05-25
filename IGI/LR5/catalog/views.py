from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required

from .models import Vehicle

from .forms import VehicleForm

from django.core.paginator import Paginator


def vehicle_list(request):

    vehicles = Vehicle.objects.all()

    paginator = Paginator(
        vehicles,
        5
    )

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)
    
    search = request.GET.get('search')

    sort = request.GET.get('sort')

    if search:

        vehicles = vehicles.filter(
            brand__icontains=search
        )

    if sort == 'brand':

        vehicles = vehicles.order_by('brand')

    elif sort == 'capacity':

        vehicles = vehicles.order_by('-load_capacity')

    return render(request, 'catalog/vehicle_list.html', {
        'vehicles': page_obj
    })


@login_required
def vehicle_create(request):

    if request.method == 'POST':

        form = VehicleForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('/vehicles/')

    else:

        form = VehicleForm()

    return render(request, 'catalog/vehicle_form.html', {
        'form': form
    })


@login_required
def vehicle_update(request, pk):

    vehicle = get_object_or_404(
        Vehicle,
        pk=pk
    )

    if request.method == 'POST':

        form = VehicleForm(
            request.POST,
            instance=vehicle
        )

        if form.is_valid():

            form.save()

            return redirect('/vehicles/')

    else:

        form = VehicleForm(instance=vehicle)

    return render(request, 'catalog/vehicle_form.html', {
        'form': form
    })


@login_required
def vehicle_delete(request, pk):

    vehicle = get_object_or_404(
        Vehicle,
        pk=pk
    )

    if request.method == 'POST':

        vehicle.delete()

        return redirect('/vehicles/')

    return render(request, 'catalog/vehicle_delete.html', {
        'vehicle': vehicle
    })