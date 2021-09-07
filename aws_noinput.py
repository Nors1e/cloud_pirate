#TODO: Convert this to a def page to call to main
import json
import boto3

#desired_region = input("Input your desired region: ")
pricing = boto3.client('pricing', region_name='us-east-1')


#sets filters for data
response = pricing.get_products(
    ServiceCode='AmazonEC2',
    Filters = [
        # TODO: let the user input filters 
        {'Type' :'TERM_MATCH', 'Field':'operatingSystem', 'Value':'Windows'                     },
        # {'Type' :'TERM_MATCH', 'Field':'vcpu',            'Value':'64'                          },
        # {'Type' :'TERM_MATCH', 'Field':'memory',          'Value':'256 GiB'                     },
        # {'Type' :'TERM_MATCH', 'Field':'location',        'Value':'US West (N. California)'     }
    ],
    MaxResults=20
)


product_attributes = {}

# stores info in a list due to overwriting and converts data into json
#TODO: add a way to include the product name, allow the user to query product information associated with that product
for entry_string in response["PriceList"]:
    entry = json.loads(entry_string)

    sku_num = entry.get('product').get('sku')
    unit_num = sku_num + '.' + 'JRTCKXETXF'
    unit_num_one = sku_num + '.' + 'JRTCKXETXF' + '.' + '6YS6EN2CT7'

    on_demand = entry["terms"]["OnDemand"].popitem()[1]
    desc_variable = on_demand.get("priceDimensions").get(unit_num_one)["description"]
    product_attributes[on_demand["sku"]] = on_demand["priceDimensions"].popitem()[1]["pricePerUnit"]
    product_attributes[on_demand["sku"]]["description"] = desc_variable


#servers sorted in ascending order based on price
sort_servers = dict(sorted(product_attributes.items(), key=lambda item: float(item[1]["USD"])))

new_servers = {}
for k,v in sort_servers.items():
    if float(v["USD"]) != 0.0000000:
        new_servers[k] = v

server_len = int(input("how many sorted servers would you like to see?"))

if server_len <= len(new_servers.keys()) and isinstance(server_len, int):
    print("hell")
else:
    print("please enter a valid number")


print(new_servers)

dict_pairs = new_servers.items()
pairs_iterator = iter(dict_pairs)
first_pair = next(pairs_iterator)

print(first_pair)

#TODO: Create a way for users to iterate through and print out a set index amount