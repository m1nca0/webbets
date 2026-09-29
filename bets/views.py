from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views import View

from bets.models import *

# Create your views here.

class ShowSportsView(View):
    def get(request, *args, **kwargs):
        sports = Sport.objects.all()

        result = ""
        for s in sports:
            result += s.name + "<br>"

        return HttpResponse(result)