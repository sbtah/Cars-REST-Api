from django.urls import reverse
from rest_framework import status
from rest_framework import test
from rest_framework.test import APITestCase
from api.models import Car, Rate


# Testcase for cars endpoint.
class CarsPostTest(APITestCase):

    # Test for GET/ cars/
    def test_get_cars(self):

        url = reverse('api:cars')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    # Test for POST/ cars/
    def test_post_cars(self):
        
        data = {
            "make": "VOLKSWAGEN",
            "model": "Passat"
        }
        url = reverse('api:cars')
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    
    def test_delete_car(self):

        self.test_car = Car.objects.create(make='VOLKSWAGEN', model='Passat')
        url = reverse('api:car', kwargs={'id': self.test_car.pk})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)


# Testcase for rate endpoint.
class RatesPostTest(APITestCase):

    # Test for POST/ rate/
    def test_post_rates(self):

        self.test_car = Car.objects.create(make='VOLKSWAGEN', model='Passat')

        data = {
            "car_id": "1",
            "rating": "5",
        }

        url = reverse('api:rate')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


# Testcase for rate endpoint.
class PopularsPostTest(APITestCase):

    # Test for  GET/ popular/
    def test_get_populars(self):
        url = reverse('api:popular')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)