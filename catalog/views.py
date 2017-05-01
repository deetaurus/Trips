from django.http import HttpResponse
from rest_framework import generics
from rest_framework.response import Response
from .models import Trips
from .serializers import TripsSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
import django_filters
import datetime
from geopy.distance import vincenty
from rest_framework.response import Response

def is_within_radius(lat,lon,q_lat,q_long,dist):
    print vincenty((float(lat),float(lon)),(float(q_lat),float(q_long))).km
    return vincenty((float(lat),float(lon)),(float(q_lat),float(q_long))).km  <= dist

class TripsList(generics.ListAPIView):
    serializer_class = TripsSerializer

    def get_queryset(self):
        queryset = Trips.objects.all()
        start_time = self.request.query_params.get('start_time', None)
        end_time = self.request.query_params.get('start_time', None)
        latitude = self.request.query_params.get('latitude', None)
        longitude = self.request.query_params.get('longitude', None)
        count = self.request.query_params.get('count', None)
        if start_time is not None and end_time is not None:
            queryset = queryset.filter(tpep_pickup_datetime__gte=start_time,tpep_dropoff_datetime__lte=end_time)

        total = 0
        for query in queryset:
            if latitude is not None and longitude is not None and is_within_radius(float(latitude),float(longitude),query.pickup_latitude,query.pickup_longitude,float(10)):
                total += 1
        print 'total:',total
        print 'count:',count
        if count <= total:
            print 'Yes'
        else:
            print 'No'
        #return Response("Yes").render()
        return queryset


'''
class ProductDetail(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''
