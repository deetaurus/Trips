from .models import Trips
from rest_framework import serializers

class TripsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trips
        fields = ('VendorID','tpep_pickup_datetime','tpep_dropoff_datetime','passenger_count','trip_distance','pickup_longitude','pickup_latitude','RatecodeID','store_and_fwd_flag','dropoff_longitude','dropoff_latitude','payment_type','fare_amount','extra','mta_tax','tip_amount','tolls_amount','improvement_surcharge','total_amount')
