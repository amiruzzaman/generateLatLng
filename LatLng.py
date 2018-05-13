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

check_gsv_status(input_file_name, output_file_name)

print('working!')