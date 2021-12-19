
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Car, Rate
from django.shortcuts import get_object_or_404
from .serializers import CarSerializer, RateSerializer, PopularCarSerializer


# cars endpoint.
class CarsView(APIView):

    # GET/ cars/
    def get(self, request, id=None):
        items = Car.objects.all()
        serializer = CarSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # POST/ cars/
    def post(self, request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE/ cars/{id}/
    def delete(self, request, id=None):
        item = get_object_or_404(Car, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})




# rate endpoint.
class RatesView(APIView):

    # POST/ rate/
    def post(self, request):
        serializer = RateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# popular endpoint.
class PopularsView(APIView):

    # GET/ popular/
    def get(self, request):
        """
        This get method is using sorted function on list of Car objects to sort them by number of rates. This is probably slow.
        """
        items = sorted(Car.objects.all(), key=lambda a: a.rates_number(), reverse=True)
        print(items)
        serializer = PopularCarSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

