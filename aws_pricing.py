import json
import boto3
 
pricing = boto3.client('pricing', region_name='us-east-1')
 
response = pricing.get_products(
     ServiceCode='AmazonEC2',
     Filters = [
         {'Type' :'TERM_MATCH', 'Field':'operatingSystem', 'Value':'Linux'              },
         {'Type' :'TERM_MATCH', 'Field':'vcpu',            'Value':'64'                   },
         {'Type' :'TERM_MATCH', 'Field':'memory',          'Value':'256 GiB'              },
         {'Type' :'TERM_MATCH', 'Field':'location',        'Value':'US East (N. Virginia)'}
     ],
     MaxResults=20
)

# stores data in json file 
with open('data.json', 'w') as fp:
    # convert the pricelist entries
    for i, entry in enumerate(response["PriceList"]):
        response["PriceList"][i] = json.loads(entry)
    json.dump(response, fp)
