#TODO: Convert this to a def page to call to main
import requests
import json

def find_machine(index):
    split_index = index.split()
    for word in split_index:
        if split_index.index(word) == 2:
            return word


print("1. North Central US (Illinois)")	
print("2. East US (Virginia)")
print("3. West US (N. California)")
print("4. South Central US (Texas)")

desired_location = int(input("Choose desired server zone: "))

# User input sorting location
if desired_location == 1:
    location_serv = 'northcentralus'
elif desired_location == 2:
    location_serv = 'eastus'
elif desired_location == 3:
    location_serv = 'westus'
elif desired_location == 4:
    location_serv = 'southcentralus'

use_case = input("What will be your use case for the")

response = requests.get(f"https://prices.azure.com/api/retail/prices?$filter=serviceName%20eq%20%27Virtual%20Machines%27%20and%20priceType%20eq%20%27Consumption%27%20and%20endswith(armRegionName,%20%27{location_serv}%27)%20and%20(startswith(skuName,%20%27D%27)%20or%20startswith(skuName,%20%27E%27)%20or%20startswith(skuName,%20%27F%27)%20or%20startswith(skuName,%20%27M%27))%20and%20endswith(skuName,%27%20Spot%27)")

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
    azure_dictionary['type'] = find_machine(response_items["Items"][i]["productName"])
    dicts.append(azure_dictionary)



sorted_dict = (sorted(dicts, key=lambda item: float(item["USD"])))

for i in sorted_dict:
    if i.get('USD') == 0.0000000:
        del i
    else:
        continue



for i in sorted_dict:
    print(i)