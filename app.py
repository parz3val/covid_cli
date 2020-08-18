import  json
import datetime
from json_output import json_output_with_requests, json_output_with_urllib
from big_block import *

url = "http://api.covid19api.com/summary"

json_file = open('saved.json','w')

try:
    print('Sending request with Requests.')
    loaded_jsn = json_output_with_requests(url)
    print('Request successful')
    
except:
    print('Sending request with URLLib.')
    loaded_jsn = json_output_with_urllib(url)
    print('Request Successful')

json.dump(loaded_jsn,json_file)


global_data = loaded_jsn['Global']
cd_data = loaded_jsn['Countries']


##Print the details of the world.
four_lines()
one_block()

from detailsblock import details_block
details_block(global_data)

one_block()
four_lines()

## Details of the country we want:

wants = 1

while wants is 1:

    country = input("Enter the name of country you want! Or, n to quit\n ")
    if country == 'n':
        thank_you()
        break

    for countries in cd_data:
        if countries['Country'] == country:
            one_block()
            details_block(countries)
            one_block()
            four_lines()

json_file.close()




