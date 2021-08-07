import requests
import json

response = requests.get("https://prices.azure.com/api/retail/prices?$filter=serviceName eq 'Virtual Machines'")

response_items = response.json()

print(type(response_items.get('Items')))

for i in response_items:
    print(i)




price_dictionary = {}
# print(response.json())

# print(type(response))

