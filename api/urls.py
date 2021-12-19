from django.urls import path
from .views import CarsView, RatesView, PopularsView

app_name = 'api'

urlpatterns = [
    path('cars/', CarsView.as_view(), name='cars'),
    path('cars/<int:id>/', CarsView.as_view(), name='car'),
    path('rate/', RatesView.as_view(), name='rate'),
    path('popular/', PopularsView.as_view(), name='popular'),
]