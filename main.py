import requests
import json
import boto3

# Finds value type using iterable position in a list of strings
    # Finds the machine type in description
def find_machine(index):
    split_index = index.split()
    for word in split_index:
        if split_index.index(word) == 2:
            return word

# Reads in file containing instance types
    # Compares grouped strings containing server descriptions to find machine type for AWS
def desc_type(desc):
    temp_list = []
    seperated_desc = desc.split()
    with open("text_files/instance_types.txt", 'r') as f:
        for i in f:
            temp_list.append(i.strip('\n'))
    for i in seperated_desc:
        if i in temp_list:
            return i


# Outputs the dictionary value of a nested dictionary 
    # Loops through nested dicts containing server information
def output(servers):
    for index, (key, value) in enumerate(servers.items()):
        if index < server_len:
            for i in key, value:
                print(f'SKU: {key}')
                print(f'Price: {value["USD"]}')
                print(f'Description: {value["description"]}')
                print(f'Type: {value["type"]} \n')

# Sorts through
    # Eliminates the prices of servers < 0.0000000
def server_zero_eliminator(sorted_servers):
    aws_cleared_servers = {}
    for key,value in sorted_servers.items():
        if float(value["USD"]) != 0.0000000:
            aws_cleared_servers[key] = value
    return aws_cleared_servers


with open("text_files/title.txt", "r") as f:
  print(f.read())

#TODO: Regionality is off for aws and azure, azure has central zones while aws is primarily east and west
print("1. US East (Ohio, Illinois)")	
print("2. US East (N. Virginia), Texas")
print("3. US West (N. California)")
print("4. US West (Oregon)")
print("\n")


# User input location
while True:
    try:
        host_location = int(input("Choose your pricing zone: "))
        break
    except ValueError:
        print("Oops please input an integer(example: 1).")
print("\n")


if host_location == 1:
    #host_serv = 'us-east-1'
    azure_location = 'eastus'
    aws_location_serv = 'US East (Ohio)'
elif host_location == 2:
    #host_serv = 'us-east-2'
    azure_location = 'eastus2'
    aws_location_serv = 'US East (N. Virginia)'
elif host_location == 3:
    #host_serv = 'us-west-1'
    azure_location = 'westus'
    aws_location_serv = 'US West (N. California)'
elif host_location == 4:
    #host_serv = 'us-west-2'
    azure_location = 'westus2'
    aws_location_serv = 'US West (Oregon)'


print("1. General Purpose(testing and development)")
print("2. Compute Optimized(webserver)")
print("3. Memory optimized(relational database)")
print("4. Storage Optimized(data warehousing)")
print("\n")


while True:
    try:
        use_case = int(input("What will be your use case for this VM? "))
        break
    except ValueError:
        print("Oops please input an integer(example: 1).")
print("\n")


if use_case == 1:
    azure_use = '(startswith(skuName,%20%27D%27))'
elif use_case == 2:
    azure_use = '(startswith(skuName,%20%27F%27))'
elif use_case == 3:
    azure_use = '(startswith(skuName,%20%27E%27))'
elif use_case == 4:
    azure_use = '(startswith(skuName,%20%27F%27))'


# AWS client pricing region, eliminated pricing region
aws_pricing = boto3.client('pricing')


# sets filters for data AWS
aws_data = aws_pricing.get_products(
    ServiceCode='AmazonEC2',
    Filters = [
        # TODO: let the user input filters 
        {'Type' :'TERM_MATCH', 'Field':'operatingSystem', 'Value':'Windows'                     },
        #{'Type' :'TERM_MATCH', 'Field':'vcpu',            'Value':'64'                          },
        #{'Type' :'TERM_MATCH', 'Field':'memory',          'Value':'256 GiB'                     },
        {'Type' :'TERM_MATCH', 'Field':'location',        'Value':aws_location_serv                 }
    ],
    MaxResults=100
)


# Sets filters Azure
response = requests.get(f"https://prices.azure.com/api/retail/prices?$filter=serviceName%20eq%20%27Virtual%20Machines%27%20and%20priceType%20eq%20%27Consumption%27%20and%20endswith(armRegionName,%20%27{azure_location}%27)%20and%20{azure_use}%20and%20endswith(skuName,%27%20Spot%27)")
azure_data = response.json()

# ****** Azure ****** 
azure_dictionary = {}
for i in range(len(azure_data["Items"])):
    # retrieve price
    azure_dictionary[azure_data["Items"][i]['skuId']] = {'USD': azure_data["Items"][i]['unitPrice']}
    # retrieve SKU
    azure_dictionary[azure_data["Items"][i]['skuId']]['description'] = azure_data["Items"][i]["productName"]
    # retrieves machine sub type
    azure_dictionary[azure_data["Items"][i]['skuId']]['type'] = find_machine(azure_data["Items"][i]["productName"])



# ******** AWS *********
product_attributes = {}
# stores info in a list due to overwriting and converts data into json
for entry_string in aws_data["PriceList"]:
    entry = json.loads(entry_string)

    # path variables
    sku_num = entry.get('product').get('sku')
    unit_num = sku_num + '.' + 'JRTCKXETXF'
    unit_num_one = sku_num + '.' + 'JRTCKXETXF' + '.' + '6YS6EN2CT7'

    # isolates required on demand data
    on_demand = entry["terms"]["OnDemand"].popitem()[1]
    # adds path to product description in on_demand
    desc_variable = on_demand.get("priceDimensions").get(unit_num_one)["description"]
    # pops USD and appends it to the associated sku in product attributes
    product_attributes[on_demand["sku"]] = on_demand["priceDimensions"].popitem()[1]["pricePerUnit"]
    # adds description to sku
    product_attributes[on_demand["sku"]]["description"] = desc_variable
    # adds server type to sku
    product_attributes[on_demand["sku"]]["type"] = desc_type(product_attributes[on_demand["sku"]]["description"])



# Servers sorted in descending order based on price
aws_sort_price = dict(sorted(product_attributes.items(), key=lambda item: float(item[1]["USD"])))

azure_sorted_dict = {key: azure_dictionary[key] for key in sorted(azure_dictionary, key=lambda item: float(azure_dictionary[item]["USD"]))}



server_len = int(input("How many servers would you like to see? "))

print("\n **** Azure ****")

output(azure_sorted_dict)

print("----------------------------------------------------------------")
print("\n **** AWS ****")

output(server_zero_eliminator(aws_sort_price))