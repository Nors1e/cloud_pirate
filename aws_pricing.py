import json
import boto3
import objectpath
import pprint
 
pricing = boto3.client('pricing', region_name='us-east-1')
 
print("Selected EC2 Products")
print("=====================")
 
response = pricing.get_products(
     ServiceCode='AmazonEC2',
     Filters = [
         {'Type' :'TERM_MATCH', 'Field':'operatingSystem', 'Value':'Linux'              },
         {'Type' :'TERM_MATCH', 'Field':'vcpu',            'Value':'64'                   },
         {'Type' :'TERM_MATCH', 'Field':'memory',          'Value':'256 GiB'              },
         {'Type' :'TERM_MATCH', 'Field':'location',        'Value':'US East (N. Virginia)'}
     ],
     MaxResults=1
)

# print(response['PriceList'])

#displays all ec2 info organized
for price in response['PriceList']:
 pp = pprint.PrettyPrinter(indent=1, width=300)
 pp.pprint(json.loads(price))
print()
# with open('data.json', 'w') as f:
#  f.write(json.dumps(response.get(pricing, f)))

# with open('data.json', 'w') as f:
#  json.dumps(pricing.get(response['PriceList'], f))

# with open('data.json', 'w') as fp:
#     foo = json.dumps(response['PriceList'])
#     print(foo)