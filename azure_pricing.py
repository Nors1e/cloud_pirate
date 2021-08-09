import requests
import json

# def azure_response(location,value):
#     for i in range(len(response_items["Items"])):
#         if response_items["Items"][i][str(location)] == 'US Central':
#         #retrieves price
#         azure_dictionary['unitPrice'] = response_items["Items"][i]['unitPrice']
#         #retrieve SKU
#         azure_dictionary['SKU'] = response_items["Items"][i]['skuId']

response = requests.get("https://prices.azure.com/api/retail/prices?$filter=serviceName eq 'Virtual Machines'")

response_items = response.json()

azure_dictionary = {}
for i in range(len(response_items["Items"])):
    if response_items["Items"][i]["location"] == 'US Central':
        #retrieve price
        azure_dictionary['unitPrice'] = response_items["Items"][i]['unitPrice']
        #retrieve SKU
        azure_dictionary['SKU'] = response_items["Items"][i]['skuId']
        #operating system???

print(azure_dictionary)
