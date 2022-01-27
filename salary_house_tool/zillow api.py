import http.client
from http.client import HTTPSConnection

conn: HTTPSConnection = http.client.HTTPSConnection("zillow-com1.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "zillow-com1.p.rapidapi.com",
    'x-rapidapi-key': "cb6f3e5942mshebaa6e32f044558p118cc0jsn79d2135f5493"
}

conn.request("GET", "/propertyExtendedSearch?location=santa%20monica%2C%20ca&home_type=Houses", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode('utf-8'))
