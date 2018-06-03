# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 09:30:26 2018

@author: mamiruzz
"""

import random
import sys
import math
import os

latitude = 34.0543543
longitude = -118.2586675
csv_file = 'random_lat_lon'
file_type = 'csv'
number_of_lat_lng = 20

def generate_random_lat_lng_data(lat, lon, num_rows, file_name, file_type):
    
    file_name = file_name + '.' + file_type
    if os.path.isfile(file_name)!=True:
        with open(file_name, 'a') as f:
            f.write('ID, Num, Lat, Lng\n')
    
    with open(file_name, 'a') as output:
        i = 0
        for _ in range(num_rows):
            hex1 = '%012x' % random.randrange(16**12)                
            flt = float(random.randint(0,100))
            dec_lat = random.random()/100
            dec_lon = random.random()/100
            #output.write('{}, {}, {}, {}, {}\n'.format(str(TripId), Lat, Lng, fi, SaveLoc+'/'+fi))
            output.write('%s, %.1f, %.6f, %.6f \n' % (hex1.lower(), i, lat+dec_lat, lon+dec_lon, ))
            i = i + 1
            #output.write('{%.6f}, {%.6f}\n'%(lon+dec_lon, lat+dec_lat))
    print('Lat Lng Generation Complete!')

#generate_random_lat_lng_data(latitude, longitude, number_of_lat_lng, csv_file, file_type)
    
    
    
##############how to pass param
import requests

url = 'http://maps.googleapis.com/maps/api/directions/json'

params = dict(
    origin='Chicago,IL',
    destination='Los+Angeles,CA',
    waypoints='Joplin,MO|Oklahoma+City,OK',
    sensor='false'
)

resp = requests.get(url=url, params=params)
data = resp.json() # Check the JSON Response Content documentation below

#print(data)

###############################


import requests

lat_lng = "34.0543543,-118.2586675"

def has_street_view(query):
    key = "&key=" + "AIzaSyDtg4UBLsMiVlnvFXy7HueEPLWypTQj2h4" #secrets.api_key


    
    host = 'https://maps.googleapis.com/maps/api/streetview/metadata?size=720x405&location=%s%s&heading=132&&pitch=-5' % (query, key)
    url = str(host)
    #print(url)

    r = requests.get(url)

    results = r.json()

    error_message = results.get('error_message')
    status = results.get('status')
    return status


#print(has_street_view(lat_lng))

import csv


input_file_name = 'random_lat_lon.csv'
output_file_name = 'output.csv'

#file = open(file_name)
#reader = csv.reader(file)
#
############appending new column header##########
#header = next(reader)
#header.append('Status')
#print(header)
#
#firstline = True
#
#for line in reader:
#    if firstline:#skip first line
#        firstline = False
#        continue
#    lat_lng_row = line[2] + ', ' + line[3]
#    lat_lng_row = ''.join( c for c in str(lat_lng_row) if  c not in "[']")
#    print(lat_lng_row)
#    print(has_street_view(lat_lng_row))

import csv

def check_gsv_status(input_file, output_file):
    with open(input_file,'r') as csvinput:
        with open(output_file, 'w') as csvoutput:
            writer = csv.writer(csvoutput, lineterminator='\n')
            reader = csv.reader(csvinput)
            
            all = []
            row = next(reader)
            row.append('Status')
            all.append(row)
            
            for row in reader:
                lat_lng_row = row[2] + ', ' + row[3]
                lat_lng_row = ''.join( c for c in str(lat_lng_row) if  c not in "[']")
                row.append(has_street_view(lat_lng_row))
                all.append(row)
                
            writer.writerows(all)
            print('Status update complete')

#check_gsv_status(input_file_name, output_file_name)
            
            
def address_from_lat_lng(query):
    key = "&key=" + "AIzaSyDtg4UBLsMiVlnvFXy7HueEPLWypTQj2h4" #secrets.api_key
    
    mylist = query.replace(' ','').split(',')
    
    
    latitude = 35.1330343
    longitude = -90.0625056
    
    lattitude = mylist[0]
    longitude = mylist[1]

    # Did the geocoding request comes from a device with a
    # location sensor? Must be either true or false.
    sensor = 'true'

    # Hit Google's reverse geocoder directly
    # NOTE: I *think* their terms state that you're supposed to
    # use google maps if you use their api for anything.
    base = "http://maps.googleapis.com/maps/api/geocode/json?"
    params = "latlng={lat},{lon}&sensor={sen}".format(
        lat=latitude,
        lon=longitude,
        sen=sensor
    )
    url = "{base}{params}".format(base=base, params=params)
    response = requests.get(url)
    return response.json()['results'][0]['formatted_address']

#print(address_from_lat_lng(lat_lng))
    

def generate_random_lat_lng_data_monte_carlo(lat, lon, num_rows, file_name, file_type):
    
    file_name = file_name + '.' + file_type
    if os.path.isfile(file_name)!=True:
        with open(file_name, 'a') as f:
            f.write('ID, Num, Lat, Lng\n')
    
    with open(file_name, 'a') as output:
        i = 0
        while i < num_rows:
            hex1 = '%012x' % random.randrange(16**12)                
            flt = float(random.randint(0,100))
            dec_lat = random.random()/100
            dec_lon = random.random()/100
            #output.write('{}, {}, {}, {}, {}\n'.format(str(TripId), Lat, Lng, fi, SaveLoc+'/'+fi))
            gen_lat = lat+dec_lat
            gen_lng = lon+dec_lon
            
            lat_lng_row = str(gen_lat) + ', ' + str(gen_lng)
            lat_lng_row = ''.join( c for c in str(lat_lng_row) if  c not in "[']")
            if(has_street_view(lat_lng_row)=='OK'):
                output.write('%s, %.1f, %.6f, %.6f \n' % (hex1.lower(), i, gen_lat , gen_lng, ))
                print(has_street_view(lat_lng_row))
                print('status')
                i = i + 1
            else:
                print(has_street_view(lat_lng_row))
            #output.write('{%.6f}, {%.6f}\n'%(lon+dec_lon, lat+dec_lat))
    print('Lat Lng Generation Complete!')
#generate_random_lat_lng_data_monte_carlo(41.153953, -81.338122, 10, 'Kent_city', 'csv')


#########################################
myloc = "Kent_city" 
key = "&key=" + "AIzaSyDtg4UBLsMiVlnvFXy7HueEPLWypTQj2h4" #secrets.api_key

csv_file = myloc+'.csv'

if os.path.isfile(csv_file)!=True:
    with open(myloc+'/'+csv_file, 'a') as f:
        f.write('TripId, Lat, Lng, FileName, LinkLocation\n')


def GetStreetView(Add, SaveLoc, TripId, Lat, Lng, FileNo):
    import urllib.parse
    query = urllib.parse.quote(Add)
    host = 'https://maps.googleapis.com/maps/api/streetview?size=720x405&location=%s%s&heading=132&&pitch=-5' % (query, key)
    MyUrl = str(host)
    print(MyUrl)
    fi = Add + ".jpg"
    fi = SaveLoc+'-'+str(FileNo) +'.jpg'
    with open(SaveLoc+'/'+csv_file, 'a') as f:
        f.write('{}, {}, {}, {}, {}\n'.format(str(TripId), Lat, Lng, fi, SaveLoc+'/'+fi))
        print('csv')    
    try:
        os.makedirs(SaveLoc)
    except OSError as e:
        if e.errno != 17:
            raise # not EEXISTS
    #urllib.urlretrieve(MyUrl, os.path.join(SaveLoc,fi))
    urllib.request.urlretrieve(MyUrl, os.path.join(SaveLoc, fi))
    
    
    
    if fi not in Sizes:
        return
    for size in Sizes[fi]:
        if os.path.getsize(os.path.join(SaveLoc, fi)) == size:
            os.remove(os.path.join(SaveLoc, fi))
            return


#Tests = ["34.0543543,-118.2586675",
#    "34.0542833,-118.2587341",
#    "41.076711,-81.519083"]

Sizes = dict()



import csv

results = []



source_file = 'kent_city.csv'
with open(source_file, newline='') as myFile:  
    reader = csv.reader(myFile)
    lat_lng = ""
    firstline = True
    i = 0
    for row in reader:
        if firstline:    #skip first line
            firstline = False
            continue
        results.append(str(row[0]))
        id_value = row[0]
        lat = str(row[2])
        lng = str(row[3])
        row = row[2] +',' + row[3]
        
        row = ''.join( c for c in str(row) if  c not in "[']")
        #GetStreetView(Add=row, SaveLoc=myloc, TripId = id_value, FileNo=i)
        GetStreetView(Add=row, SaveLoc=myloc, TripId = id_value, Lat=lat, Lng = lng, FileNo=i)
        print(i)
        if row[0] in (None, ","):
             break
        i+=1    
    
#########################################

print('working!')

#https://www.latlong.net/convert-address-to-lat-long.html