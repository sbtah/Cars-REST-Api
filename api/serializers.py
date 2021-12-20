from rest_framework import serializers
import requests
from .models import Car, Rate


# A serializer class for Car Model
class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ('id', 'make', 'model', 'avg_rating')
    
    # a Custom validate method that checks if POST/ car/ exists in specified API.
    def validate(self, data):
        """
        Check that Car exists in API.
        """
        API_URL = f"https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/{data['make'].upper()}?format=json"
        SEARCH_FOR_MODEL = data['model'].title()
        
        r = requests.get(API_URL)
        models = r.json()
        result = next((car for car in models["Results"] if car["Model_Name"] == SEARCH_FOR_MODEL), None,)
        if result is None:
            raise serializers.ValidationError("This Car does not exist.")
        else:
            data['make'] = result.get('Make_Name')
            data['model'] = result.get('Model_Name')
            return data
 

# A serializer class for Rate Model
class RateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rate
        fields = '__all__'


# A serializer class for Car modelm, used for GET/ popular/ endpoint.
class PopularCarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ('id', 'make', 'model', 'rates_number')