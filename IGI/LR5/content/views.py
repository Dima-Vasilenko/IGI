from django.shortcuts import render
from .models import (
    News,
    FAQ,
    Vacancy,
    Review,
    PromoCode,
    ContactEmployee,
    CompanyInfo
)
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from .forms import ReviewForm
import requests
from django.contrib.auth.decorators import login_required

def news_list(request):
    news = News.objects.all()

    return render(request, 'content/news_list.html', {
        'news': news
    })


def faq_list(request):
    faq = FAQ.objects.all()

    return render(request, 'content/faq_list.html', {
        'faq': faq
    })


def vacancy_list(request):
    vacancies = Vacancy.objects.all()

    return render(request, 'content/vacancy_list.html', {
        'vacancies': vacancies
    })


def review_list(request):
    reviews = Review.objects.all()

    return render(request, 'content/review_list.html', {
        'reviews': reviews
    })

@login_required
def add_review(request):

    if request.method == 'POST':

        form = ReviewForm(request.POST)

        if form.is_valid():

            review = form.save(commit=False)

            review.user = request.user

            review.save()

            return redirect('/reviews/')

    else:

        form = ReviewForm()

    return render(request, 'content/add_review.html', {
        'form': form
    })


@login_required
def random_driver(request):

    response = requests.get(
        'https://randomuser.me/api/'
    )

    data = response.json()

    user = data['results'][0]

    return render(request, 'content/random_driver.html', {
        'user': user
    })


@login_required
def currency_rates(request):

    response = requests.get(
        'https://api.exchangerate-api.com/v4/latest/USD'
    )

    data = response.json()

    return render(request, 'content/currency.html', {
        'rates': data['rates']
    })


def contacts_view(request):

    employees = ContactEmployee.objects.all()

    return render(
        request,
        'content/contacts.html',
        {
            'employees': employees
        }
    )


def company_view(request):

    company = CompanyInfo.objects.first()

    return render(
        request,
        'content/company.html',
        {
            'company': company
        }
    )
