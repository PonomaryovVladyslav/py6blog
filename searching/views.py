from django.http import HttpResponse
from django.shortcuts import render


def searching(request):
    return render(request, 'searching.html')
