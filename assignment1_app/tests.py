# from django.test import TestCase
import json
import urllib,urllib.request

url= 'http://stat.data.abs.gov.au/sdmx-json/data/CAPEX/1+3+2.1+2+999.P01+P02+P98+-.0+7.10+20+30.Q/all?startTime=2016-Q1&endTime=2019-Q1&dimensionAtObservation=allDimensions'

json_obj= urllib.request.urlopen(url)


data= json.load(json_obj)

for item in data['structure']['dimensions']['observation']:
    data=item



# print (data)    