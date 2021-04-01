"""
Method 	Description
delete(url, args) 	Sends a DELETE request to the specified url
get(url, params, args) 	Sends a GET request to the specified url
head(url, args) 	Sends a HEAD request to the specified url
patch(url, data, args) 	Sends a PATCH request to the specified url
post(url, data, json, args) 	Sends a POST request to the specified url
put(url, data, args) 	Sends a PUT request to the specified url
request(method, url, args) 	Sends a request of the specified method to the specified url
"""
import requests

r = requests.get("https://financialmodelingprep.com/login")
print(r.text)
print(r.status_code)

# url = "www.something.com"
# data = {
#     "p1":4,
#     "p2":8
# }
# r2 = requests.post(url=url,data=data)