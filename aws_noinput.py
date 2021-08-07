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
         {'Type' :'TERM_MATCH', 'Field':'operatingSystem', 'Value':'Linux'                       },
         {'Type' :'TERM_MATCH', 'Field':'vcpu',            'Value':'64'                          },
         {'Type' :'TERM_MATCH', 'Field':'memory',          'Value':'256 GiB'                     },
         {'Type' :'TERM_MATCH', 'Field':'location',        'Value':'US West (N. California)'     }
     ],
     MaxResults=20
)



for entry_string in response["PriceList"]:
    #converts json object data to dictionary
    entry = json.loads(entry_string)


for key in foo.get('product', {}).get('attributes', {}):
    #prints key's
    print(key)


# # store information in dictionary
product_attributes = {}


# for item in [entry]:
#     retrieved_item = item.get("product",{}).get("attributes",{}).get(str(usr_input), {})
#     product_attributes[str(usr_input)] = retrieved_item

# print("Your saved dict: ", product_attributes)