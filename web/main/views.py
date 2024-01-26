from .forms import ReservationForm
from .models import Reservation
from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import re
import datetime


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
reg_phone = re.compile('(\+7|8)\D*\d{3}\D*\d{3}\D*\d{2}\D*\d{2}')
count_tables = {}


def create(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid() \
                and re.fullmatch(regex, (form.cleaned_data.get('email'))) \
                and reg_phone.search((str(form.cleaned_data.get('phone_number')))) \
                and int(form.cleaned_data.get('date').day) \
                + int(form.cleaned_data.get('date').month) * 100 \
                + int(form.cleaned_data.get('date').year) * 10000 >= \
                int(datetime.date.today().day) \
                + int(datetime.date.today().month) * 100 \
                + int(datetime.date.today().year) * 10000 \
                and int(form.cleaned_data.get('count_hour')) >= 1 \
                and 0 <= int(form.cleaned_data.get('time')) <= 23:

            if count_tables.get(str(form.cleaned_data.get('date'))) is None:
                count_tables[str(form.cleaned_data.get('date'))] = [0 for _ in range(24)]
                for i in range(9, 21):
                    count_tables[str(form.cleaned_data.get('date'))][i] = 20
            for i in range(int(form.cleaned_data.get('count_hour'))):
                if count_tables[str(form.cleaned_data.get('date'))][i+int(form.cleaned_data.get('time'))] < \
                        int(form.cleaned_data.get('count')):
                    return redirect('error_book')
            for i in range(int(form.cleaned_data.get('count_hour'))):
                count_tables[str(form.cleaned_data.get('date'))][i+int(form.cleaned_data.get('time'))] -= \
                    int(form.cleaned_data.get('count'))
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

def error_book(request):
    return render(request, 'main/error_book.html')

def success(request):
    return render(request, 'main/success.html')


@login_required
def records(request):
    reservations = Reservation.objects.all()
    return render(request, 'main/records.html', {'reservations': reservations})


@login_required
def delete_record(request, record_id):
    Reservation.objects.filter(id=record_id).delete()
    return render(request, 'main/delete_success.html')


@login_required
def delete_success(request):
    return render(request, 'main/delete_success.html')
