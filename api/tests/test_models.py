from django.test import TestCase
from api.models import Car, Rate


# Car model test for ratings.
class Test_Car_Ratings(TestCase):

    def setUp(self):
        self.test_car = Car.objects.create(make='VOLKSWAGEN', model='Passat')
        self.test_rate = Rate.objects.create(car_id=self.test_car, rating=5)

    def test_rates_number(self):
        car = Car.objects.get(id=1)
        self.assertEqual(car.make, 'VOLKSWAGEN')
        self.assertEqual(car.model, 'Passat')
        self.assertEqual(car.rates_number(), 1)
        self.assertEqual(car.avg_rating(), 5)


# Test Car model if no ratings given.
class Test_Car_Ratings_0(TestCase):

    def setUp(self):
        self.test_car = Car.objects.create(make='VOLKSWAGEN', model='Passat')
    
    def test_rates_number(self):
        car = Car.objects.get(id=1)
        self.assertEqual(car.make, 'VOLKSWAGEN')
        self.assertEqual(car.model, 'Passat')
        self.assertEqual(car.rates_number(), 0)
        self.assertEqual(car.avg_rating(), 0)