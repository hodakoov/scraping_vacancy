from django.shortcuts import render
from scraping.models import Vacancy


def home(request):
    print(request.GET)
    qs = Vacancy.objects.all()
    return render(request, 'scraping/home.html', context={'objects_list': qs})
