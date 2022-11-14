import datetime

from django.shortcuts import render


def home(request):
    date = datetime.datetime.now().date()
    name = 'Valery'
    _context = {'date': date, 'name': name}
    return render(request, 'base.html', context=_context)