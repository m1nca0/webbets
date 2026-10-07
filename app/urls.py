"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from bets import views
from bets.api import SportsViewset
from bets.api import OutcomeViewset
from bets.api import BetViewset
from bets.api import EventViewset
from bets.api import TeamViewset
from bets.api import TournametViewset

router = DefaultRouter()
router.register('sports', SportsViewset, basename='sports')
router.register('outcome', OutcomeViewset, basename='outcome')
router.register('bet', BetViewset, basename='bet')
router.register('event', EventViewset, basename='event')
router.register('team', TeamViewset, basename='team')
router.register('tournamet', TournametViewset, basename='tournamet')


urlpatterns = [
    path('', views.ShowSportsView.as_view()),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]