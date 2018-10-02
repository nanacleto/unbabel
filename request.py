import requests


class unbable:

   url = "http://104.199.15.101/api/return_eu_countries/"

   def __init__(self):
     pass



   rq = requests

   headers = {}
   headers["cache-control"] = "no-cache"
   headers["Content-Type"] = "application/json"

   x ={"country_list": ["BE", "DE", "NY"]}


   print  headers
   print  x

   response = rq.post(url, headers=headers, json=x)



   print  headers
   print  x

   response = rq.post(url, headers=headers, json=x)


   print response.status_code
   print response.content
   print response.elapsed


