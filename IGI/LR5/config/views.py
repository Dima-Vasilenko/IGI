from django.shortcuts import render
from content.models import News


def home(request):

    latest_news = News.objects.order_by('-created_at').first()

    return render(request, 'home.html', {
        'latest_news': latest_news
    })