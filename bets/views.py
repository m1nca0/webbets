from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views import View
from django.views.generic import TemplateView

from bets.models import *

# Create your views here.

class ShowSportsView(TemplateView):
    template_name = "bets/show_sports.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sports'] = Sport.objects.all()
        return context
