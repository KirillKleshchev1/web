from .forms import ReservationForm
from .models import Reservation
from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
import re


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
reg_phone = re.compile('(\+7|8)\D*\d{3}\D*\d{3}\D*\d{2}\D*\d{2}')


def create(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid() \
                and re.fullmatch(regex, (form.cleaned_data.get('email'))) \
                and str(form.cleaned_data.get('count')).isdigit() \
                and reg_phone.search((str(form.cleaned_data.get('phone_number')))):
            form.save()
            return redirect('success')
        else:
            return redirect('error')
    form = ReservationForm()
    data = {
        'form': form,
    }
    return render(request, 'main/create.html', data)


def error(request):
    return render(request, 'main/error.html')


def success(request):
    return render(request, 'main/success.html')


@login_required
def records(request):
    reservations = Reservation.objects.all()
    return render(request, 'main/records.html', {'reservations': reservations})
