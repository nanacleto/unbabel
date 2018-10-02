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

<<<<<<< HEAD

=======
>>>>>>> fcbc69580d679f4100e6998a1b008c62799759ce
   print  headers
   print  x

   response = rq.post(url, headers=headers, json=x)

<<<<<<< HEAD


   print  headers
   print  x

   response = rq.post(url, headers=headers, json=x)


=======
>>>>>>> fcbc69580d679f4100e6998a1b008c62799759ce
   print response.status_code
   print response.content
   print response.elapsed


