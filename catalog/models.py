# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Trips(models.Model):
    VendorID = models.IntegerField()
    tpep_pickup_datetime =  models.DateTimeField()
    tpep_dropoff_datetime =  models.DateTimeField()
    passenger_count	=  models.TextField()
    trip_distance = models.TextField()
    pickup_longitude =   models.FloatField()
    pickup_latitude	=   models.FloatField()
    RatecodeID  = models.TextField()
    store_and_fwd_flag  = models.TextField()
    dropoff_longitude  = models.FloatField()
    dropoff_latitude = models.FloatField()
    payment_type  = models.TextField()
    fare_amount  =  models.TextField()
    extra = models.TextField()
    mta_tax =  models.TextField()
    tip_amount  = models.TextField()
    tolls_amount  = models.TextField()
    improvement_surcharge	 = models.TextField()
    total_amount = models.TextField()
