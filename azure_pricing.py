#TODO: Convert this to a def page to call to main
import requests
import json




response = requests.get("https://prices.azure.com/api/retail/prices?$filter=serviceName eq 'Virtual Machines'")

response_items = response.json()



dicts = []
for i in range(len(response_items["Items"])):
    azure_dictionary = {}
    azure_dictionary['sku'] = response_items["Items"][i]['skuId']
    azure_dictionary['location'] = response_items["Items"][i]["location"]
    #retrieve price
    azure_dictionary['USD'] = response_items["Items"][i]['unitPrice']
    #retrieve SKU
    azure_dictionary['description'] = response_items["Items"][i]["productName"]
    azure_dictionary['location'] = response_items["Items"][i]["location"]
    dicts.append(azure_dictionary)
for i in dicts:
    print(i)



# sorted_azure = dict(sorted(dicts.items(), key=lambda item: item[1]))
# print(sorted_azure)

# azure_dictionary = {}
# for i in range(len(response_items["Items"])):
#     #retrieve price
#     azure_dictionary['unitPrice'] = response_items["Items"][i]['unitPrice']
#     #retrieve SKU
#     azure_dictionary['sku'] = response_items["Items"][i]['skuId']
#     azure_dictionary['description'] = response_items["Items"][i]["productName"]
#     azure_dictionary['location'] = response_items["Items"][i]["location"]
# print(azure_dictionary)