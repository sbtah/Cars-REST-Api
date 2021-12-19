from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Car model.
class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    
    # Custom method for calculating number of rates for particular instance of Car.
    def rates_number(self):
        """
        Returns a number of rates for instance of Car.
        """
        ratings = Rate.objects.filter(car_id=self)
        return ratings.count()

    # Method for calculating average rate for instance of Car.
    def avg_rating(self):
        """
        Returns an average rating for instance of Car.
        """
        sum = 0
        ratings = Rate.objects.filter(car_id=self)
        for i in ratings:
            sum += i.rating
        if ratings.count() > 0:
            return round(sum / ratings.count(), 2)
        else:
            return 0
    
    # Custom Save, dunno if this is still needed, since serializer is saving data from external API.
    def save(self, *args, **kwargs):
        self.make = self.make.upper()
        self.model = self.model.capitalize()
        return super(Car, self).save(*args, **kwargs)


# Rating model.
class Rate(models.Model):
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
