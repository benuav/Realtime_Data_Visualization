import csv 
import random
import time
from datetime import datetime


currentTime = datetime.now()
indexNumber = 0
lat = -27.552510
lng = 153.053360
number = 8

def rand (): # <= fake random number from 0 to 16.
    number = []
    for i in range(9):
        number.append(random.randint(0,16))
    number.sort()
    return number[4]



fieldnames = ["indexNumber", "time", "latitude", "longitude", "resultNumber"]

with open('./data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
    csv_writer.writeheader()

while indexNumber != 1001:#<- set the time
    with open('./data.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)

        info = {
            'indexNumber': indexNumber,
            'time': currentTime,
            'latitude': lat,
            'longitude': lng,
            'resultNumber': number
        }

        csv_writer.writerow(info)
        print(indexNumber, currentTime, round(lat,6), round(lng,6), number)

        indexNumber += 1 #import realtime , how?
        currentTime = datetime.now() # get the current time
        lat =  lat # moving south 1 meter "{:.2f}".format(a_float)
        lng -= 0.00002 # moving west 2 meter by - 0.00002
        number = rand()
#        for i in range(5):
#            number.append(random.randint(0,16))
#        number.sort()
#        number = number[2]

    time.sleep(1)
    
#in order to run this properly, python file need to run in pycharm, web need host on python server in VScode
# when use python server, change csv number will not refresh the page // python3 -m http.server
#python command to run:  python CSVs_live_data.py //python3 -m http.server

# python3 -m http.server -> http://[::]:8000/views/
