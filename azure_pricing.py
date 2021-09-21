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


print("1. General Purpose(testing and development)D")
print("2. Compute Optimized(webserver)F")
print("3. Memory optimized(relational database)E")
print("4. Storage Optimized(data warehousing)L")
use_case = int(input("What will be your use case for this VM? "))

if use_case == 1:
    foo = '(startswith(skuName,%20%27D%27))'
elif use_case == 2:
    foo = '(startswith(skuName,%20%27F%27))'
elif use_case == 3:
    foo = '(startswith(skuName,%20%27E%27))'
elif use_case == 4:
    foo = '(startswith(skuName,%20%27F%27))'

# (startswith(skuName,%20%27D%27)%20or%20startswith(skuName,%20%27E%27)%20or%20startswith(skuName,%20%27F%27)%20or%20startswith(skuName,%20%27M%27))%20and%20endswith(skuName,%27%20Spot%27)
response = requests.get(f"https://prices.azure.com/api/retail/prices?$filter=serviceName%20eq%20%27Virtual%20Machines%27%20and%20priceType%20eq%20%27Consumption%27%20and%20endswith(armRegionName,%20%27{location_serv}%27)%20and%20{foo}%20and%20endswith(skuName,%27%20Spot%27)")

response_items = response.json()


# dicts = []
# for i in range(len(response_items["Items"])):
#     azure_dictionary = {}
#     azure_dictionary['sku'] = response_items["Items"][i]['skuId']
#     #retrieve price
#     azure_dictionary['sku']['USD'] = response_items["Items"][i]['unitPrice']
#     #retrieve SKU
#     azure_dictionary['sku']['description'] = response_items["Items"][i]["productName"]
#     azure_dictionary['sku']['type'] = find_machine(response_items["Items"][i]["productName"])
#     dicts.append(azure_dictionary)

dicts = []
azure_dictionary = {}
for i in range(len(response_items["Items"])):
    #retrieve price
    azure_dictionary[response_items["Items"][i]['skuId']] = {'USD': response_items["Items"][i]['unitPrice']}
    #retrieve SKU
    azure_dictionary[response_items["Items"][i]['skuId']]['description'] = response_items["Items"][i]["productName"]
    azure_dictionary[response_items["Items"][i]['skuId']]['type'] = find_machine(response_items["Items"][i]["productName"])

print(azure_dictionary)

# dicts = []
# for i in range(len(response_items["Items"])):
#     azure_dictionary = {}
#     # azure_dictionary = response_items["Items"][i]['skuId']
#     #retrieve price
#     azure_dictionary[response_items["Items"][i]['skuId']] = {'USD': response_items["Items"][i]['unitPrice']}
#     print(azure_dictionary)
#     azure_dictionary['sku']['USD'] = response_items["Items"][i]['unitPrice']
#     #retrieve SKU
#     azure_dictionary['sku']['description'] = response_items["Items"][i]["productName"]
#     azure_dictionary['sku']['type'] = find_machine(response_items["Items"][i]["productName"])
#     dicts.append(azure_dictionary)


# Sorts items based on price
print(dicts)
sorted_dict = {key: azure_dictionary[key] for key in sorted(azure_dictionary, key=lambda item: float(azure_dictionary[item]["USD"]))}

print(sorted_dict)

# removes items if they fall below threashold
# for i in sorted_dict:
#     if i.get('USD') == 0.0000000:
#         del i
#     else:
#         continue

server_len = int(input("how many servers would you like to see?"))

for index, (key, value) in enumerate(sorted_dict.items()):
    if index < server_len:
        print(key, value)


