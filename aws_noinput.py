import json
import boto3

#def that takes in required data via text file

#desired_region = input("Input your desired region: ")
pricing = boto3.client('pricing', region_name='us-east-1')


#sets filters for data
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


for entry_string in response["PriceList"]:
    #converts json object data to dictionary
    entry = json.loads(entry_string)


# creates dictionary
product_attributes = {}

sku_num = entry.get('product').get('sku')
unit_num = sku_num + '.' + 'JRTCKXETXF'
unit_num_one = sku_num + '.' + 'JRTCKXETXF' + '.' + '6YS6EN2CT7'

for item in [entry]:
    price = entry.get('terms').get('OnDemand').get(unit_num).get('priceDimensions').get(unit_num_one)
    product_attributes['sku'] = sku_num
    product_attributes['price'] = price



print("Your saved dict: ", product_attributes)