# Full path and name to your csv file
csv_filepathname="/Users/deepthiravisankar/Documents/InterviewPrep/RevMax/Trips/trip_data.csv"

# Full path to your django project directory
your_djangoproject_home="."

from catalog.models import Trips
import csv

dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')
count  = 0
for row in dataReader:
    if count != 0: # Ignore the header row, import everything else
        trips = Trips()
        trips.VendorID = row[0]
        trips.tpep_pickup_datetime =  row[1]
        trips.tpep_dropoff_datetime =  row[2]
        trips.passenger_count	=  row[3]
        trips.trip_distance = row[4]
        trips.pickup_longitude =   row[5]
        trips.pickup_latitude	=   row[6]
        trips.RatecodeID  = row[7]
        trips.store_and_fwd_flag  = row[8]
        trips.dropoff_longitude  = row[9]
        trips.dropoff_latitude = row[10]
        trips.payment_type  = row[11]
        trips.fare_amount  =  row[12]
        trips.extra = row[13]
        trips.mta_tax =  row[14]
        trips.tip_amount  = row[15]
        trips.tolls_amount  = row[16]
        trips.improvement_surcharge	 = row[17]
        trips.total_amount = row[18]
        #print trips
        trips.save()
    count += 1
