import requests
import json_countries as county

class unbable:

   url =   "http://104.199.15.101/api/return_eu_countries"

   def __init__(self ):
     pass


   rq = requests

   response = rq.put(url, data=county.BE)

   print response.content

