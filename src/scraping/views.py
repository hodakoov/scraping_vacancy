from django.shortcuts import render

from scraping.forms import FindForm
from scraping.models import Vacancy


def home(request):
    # print(request.GET)
    form = FindForm()
    city = request.GET.get('city')
    language = request.GET.get('language')
    qs = []
    if city or language:
        _filter = {}
        if city:
            _filter["city__slug"] = city
        if language:
            _filter["language__slug"] = language

        qs = Vacancy.objects.filter(**_filter)

    return render(request, 'scraping/home.html', context={'objects_list': qs,
                                                          'form': form})
