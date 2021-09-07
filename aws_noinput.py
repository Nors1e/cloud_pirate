#TODO: Convert this to a def page to call to main

import json
import boto3

pricing = boto3.client('pricing', region_name='us-east-1')

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


# sets filters for data
response = pricing.get_products(
    ServiceCode='AmazonEC2',
    Filters = [
        # TODO: let the user input filters 
        {'Type' :'TERM_MATCH', 'Field':'operatingSystem', 'Value':'Windows'                     },
        {'Type' :'TERM_MATCH', 'Field':'vcpu',            'Value':'64'                          },
        {'Type' :'TERM_MATCH', 'Field':'memory',          'Value':'256 GiB'                     },
        {'Type' :'TERM_MATCH', 'Field':'location',        'Value':'US West (N. California)'     }
    ],
    MaxResults=20
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
#TODO: add a way to include the product name, allow the user to query product information associated with that product
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

print(new_servers)


server_len = int(input("how many sorted servers would you like to see?"))

#TODO: Create a way for users to iterate through and print out a set index amount
for index, (key, value) in enumerate(new_servers.items()):
    if index < server_len:
        print(key, value)