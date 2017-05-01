import datetime
import csv

csv_filepathname="/Users/deepthiravisankar/Documents/InterviewPrep/RevMax/Trips/data.csv"

def create_initial_trips(apps, schema_editor):
    Trips = apps.get_model('catalog', 'Trips')
    dataReader = csv.reader(open(csv_filepathname), delimiter=str(u',').encode('utf-8'), quotechar=str(u'"').encode('utf-8'))
    count  = 0
    for row in dataReader:
        if count != 0: # Ignore the header row, import everything else
            #print row
            trips = Trips()
            trips.VendorID = row[0]
            trips.tpep_pickup_datetime =  datetime.datetime.strptime(row[1], "%Y-%m-%d %H:%M:%S")
            trips.tpep_dropoff_datetime =  datetime.datetime.strptime(row[2], "%Y-%m-%d %H:%M:%S")
            trips.passenger_count	=  row[3]
            trips.trip_distance = row[4]
            trips.pickup_longitude =   float(row[5])
            trips.pickup_latitude	=   float(row[6])
            trips.RatecodeID  = row[7]
            trips.store_and_fwd_flag  = row[8]
            trips.dropoff_longitude  = float(row[9])
            trips.dropoff_latitude = float(row[10])
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
    print count

class Migration(migrations.Migration):

    operations = [
        migrations.RunPython(create_initial_trips),
    ]

    dependencies = [
        ('catalog', '0001_initial'),
    ]
