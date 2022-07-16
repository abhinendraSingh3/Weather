import requests
from pprint import pprint

api_key="1f2b19674274c6f15c5ad4034c757b06"

city=input("Enter the name of the city\n")

base_url="http://api.openweathermap.org/data/2.5/weather?appid="+api_key+"&q="+city

r=requests.get(base_url).json()

pprint(r)