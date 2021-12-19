from django.urls import path
from .views import CarsView, RatesView, PopularsView, home_view

app_name = 'api'

urlpatterns = [
    path('', home_view, name='home'),
    path('cars/', CarsView.as_view(), name='cars'),
    path('cars/<int:id>/', CarsView.as_view(), name='car'),
    path('rate/', RatesView.as_view(), name='rate'),
    path('popular/', PopularsView.as_view(), name='popular'),
]