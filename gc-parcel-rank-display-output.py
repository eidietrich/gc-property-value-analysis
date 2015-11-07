
# coding: utf-8

# Script to take .csv of GC ownership ranking and spit out HTML to import into BLOX
import csv

# fileName = 'gc-owner-ranking-public.csv'
# fileName = 'gc-owner-ranking-by-size.csv'
fileName = 'gc-owner-ranking-by-value.csv'

with open(fileName, 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        rank, owner, parcelnum, totval, totacres, description = row[0], row[1], row[2], row[3], row[4], row[5]
        print '<h4>' + rank + '. ' + owner + '</h4>'
        print '<p><strong>Number of parcels: </strong>'+ parcelnum + '</p>'
        print '<p><strong>Total assessed value: </strong>'+ totval + '</p>'
        print '<p><strong>Total acreage: </strong>'+ totacres + '</p>'
        print '<p>' + description + '</p> \n'
  

