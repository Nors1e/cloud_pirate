#TODO: Convert this to a def page to call to main
import requests
import json

def get_azure_holding():
response = requests.get("https://prices.azure.com/api/retail/prices?$filter=serviceName eq 'Virtual Machines'")

response_items = response.json()

azure_dictionary = {}
for i in range(len(response_items["Items"])):
        if response_items["Items"][i]["location"] == 'US Central':
            #retrieve price
            azure_dictionary['unitPrice'] = response_items["Items"][i]['unitPrice']
            #retrieve SKU
            azure_dictionary['sku'] = response_items["Items"][i]['skuId']

    return azure_dictionary