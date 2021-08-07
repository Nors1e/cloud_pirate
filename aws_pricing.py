import json
import boto3

#desired_region = input("Input your desired region: ")
pricing = boto3.client('pricing', region_name='us-east-1')

# Give all the choices in a series of print statements.
print("\n[1]US East (Ohio)")
print("[2]US East (N. Virginia)")
print("[3]US West (N. California)")
print("[4]US West (Oregon)")

    
# Ask for the user's choice.
desired_region = input("Input region: ")

if desired_region == '1':
    desired_region = 'US East (Ohio)'
elif desired_region == '2':
    desired_region = 'US East (N. Virginia)'
elif desired_region == '3':
    desired_region = 'US West (N. California)'
elif desired_region == '4':
    desired_region = 'US West (Oregon)'
else:
    print("Inoperable.")


operating_system = input("Input Operating System: ")


 
response = pricing.get_products(
     ServiceCode='AmazonEC2',
     Filters = [
         # TODO: let the user input filters 
         {'Type' :'TERM_MATCH', 'Field':'operatingSystem', 'Value':operating_system       },
         {'Type' :'TERM_MATCH', 'Field':'vcpu',            'Value':'64'                   },
         {'Type' :'TERM_MATCH', 'Field':'memory',          'Value':'256 GiB'              },
         {'Type' :'TERM_MATCH', 'Field':'location',        'Value': desired_region        }
     ],
     MaxResults=20
)


#parses through valid JSON string and converts it to python dict
for entry_string in response["PriceList"]:
    #converts json object data to dictionary
    entry = json.loads(entry_string)


for key in entry.get('product', {}).get('attributes', {}):
    #prints key's
    print(key)

usr_input = input("from the list: ")
#iterates and prints keys associated with
print(entry.get('product', {}).get('attributes', {}).get(str(usr_input), {}))

# store information in dictionary
product_attributes = {}


for item in [entry]:
    retrieved_item = item.get("product",{}).get("attributes",{}).get(str(usr_input), {})
    product_attributes[str(usr_input)] = retrieved_item

print("Your saved dict: ", product_attributes)







#TODO: If user inputs information into consol window have a program loop through the keys to determine if that value is in there based 
#on the first few letters, if no action is made after 5 seconds the program will execute and fetch data based on the first 