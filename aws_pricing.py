import json
import boto3
 
# TODO: Let the user choose their region
pricing = boto3.client('pricing', region_name='us-east-1')
 
response = pricing.get_products(
     ServiceCode='AmazonEC2',
     Filters = [
         # TODO: let the user input filters 
         {'Type' :'TERM_MATCH', 'Field':'operatingSystem', 'Value':'Linux'              },
         {'Type' :'TERM_MATCH', 'Field':'vcpu',            'Value':'64'                   },
         {'Type' :'TERM_MATCH', 'Field':'memory',          'Value':'256 GiB'              },
         {'Type' :'TERM_MATCH', 'Field':'location',        'Value':'US East (N. Virginia)'}
     ],
     MaxResults=20
)

#parses through valid JSON string and converts it to python dict for easy access
for entry_string in response["PriceList"]:
    entry = json.loads(entry_string)
    #access to keys 
print(entry['product']['attributes']['operatingSystem'])

