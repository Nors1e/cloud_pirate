#TODO: Convert this to a def page to call to main
import json
import boto3


# sorts through descriptions in dictionaries
def desc_type(desc):
    temp_list = []
    # seperates words
    seperated_desc = desc.split()
    with open("text_files/instance_types.txt", 'r') as f:
        for i in f:
            temp_list.append(i.strip('\n'))
    for i in seperated_desc:
        if i in temp_list:
            return i


#TODO: add a way to include the product name, allow the user to query product information associated with that product https://aws.amazon.com/ec2/instance-types/ (ex: compute optimized, gen purpose, etc...)

with open("text_files/title.txt", "r") as f:
  print(f.read())

print("1. US East (Ohio)")	
print("2. US East (N. Virginia)")
print("3. US West (N. California)")
print("4. US West (Oregon)")

# User input location
host_location = input("Choose your pricing zone: ")


# User input sorting location
if host_location == 1:
    location = 'us-east-2'
elif host_location == 2:
    location = 'us-east-1'
elif host_location == 3:
    location = 'us-west-1'
elif host_location == 4:
    location = 'us-west-2'
else:
    location = 'us-east-1'

# initializing client
#TODO: Add redundancy
pricing = boto3.client('pricing', region_name=location)
print("\n")


# print("1. General purpose")
# print("2. Compute optimized")
# print("3. Memory optimized")
# print("4. Storage optimized")

# server_purpose = input("Choose server requirements: ")
# print("\n")

# TODO: propose alternative instance types like compute-memory-storage
# if server_purpose == 1:
#     purpose =  # General Purpose
# elif server_purpose == 2:
#     purpose = # Compute
# elif server_purpose == 3:
#     purpose = # Memory
# elif server_purpose == 4:
#     purpose = # Storage

# server_spec = input("Choose server specifications: ") this will be like vcpu and memory

print("1. US East (Ohio)")	
print("2. US East (N. Virginia)")
print("3. US West (N. California)")
print("4. US West (Oregon)")


desired_location = int(input("Choose desired server zone: "))


# User input sorting location
if desired_location == 1:
    location_serv = 'US East (Ohio)'
elif desired_location == 2:
    location_serv = 'US East (N. Virginia)'
elif desired_location == 3:
    location_serv = 'US West (N. California)'
elif desired_location == 4:
    location_serv = 'US West (Oregon)'


keyword = input("Would you like to search via keyword(ie: SQL)(y/n)? ")
if keyword == 'y':
    # Search for keyword
else:
    # continue



print(location_serv)
print("___________________")
# sets filters for data
response = pricing.get_products(
    ServiceCode='AmazonEC2',
    Filters = [
        # TODO: let the user input filters 
        {'Type' :'TERM_MATCH', 'Field':'operatingSystem', 'Value':'Windows'                     },
        {'Type' :'TERM_MATCH', 'Field':'vcpu',            'Value':'64'                          },
        {'Type' :'TERM_MATCH', 'Field':'memory',          'Value':'256 GiB'                     },
        {'Type' :'TERM_MATCH', 'Field':'location',        'Value':location_serv                 }
    ],
    MaxResults=100
)


# products_paginator = pricing.get_paginator("get_products")
# product_responses = products_paginator.paginate(ServiceCode="AmazonEC2", Filters=[
#         # TODO: let the user input filters 
#         {'Type' :'TERM_MATCH', 'Field':'operatingSystem', 'Value':'Windows'                     },
#         {'Type' :'TERM_MATCH', 'Field':'vcpu',            'Value':'64'                          },
#         {'Type' :'TERM_MATCH', 'Field':'memory',          'Value':'256 GiB'                     },
#         {'Type' :'TERM_MATCH', 'Field':'location',        'Value':'US West (N. California)'     }
#     ])

product_attributes = {}

# stores info in a list due to overwriting and converts data into json
for entry_string in response["PriceList"]:
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



# servers sorted in ascending order based on price
sort_price = dict(sorted(product_attributes.items(), key=lambda item: float(item[1]["USD"])))


# get's rid of any servers falling below price threashold
new_servers = {}
for key,value in sort_price.items():
    if float(value["USD"]) != 0.0000000:
        new_servers[key] = value


# keyword = input("Would you like to search via keyword(ie: SQL)(y/n)? ")
# if keyword == 'y':
#     # Search for keyword
# else:
#     # continue


server_len = int(input("how many servers would you like to see?"))

# for users to iterate through and print out a set index amount
for index, (key, value) in enumerate(new_servers.items()):
    if index < server_len:
        print(key, value)