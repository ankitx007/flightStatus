from django.urls import path

from subscriptions.views import subscribe

urlpatterns = [
    path('subscribe/', subscribe, name='subscribe'),
]