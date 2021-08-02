import json
import boto3

#desired_region = input("Input your desired region: ")

# TODO: Let the user choose their region
pricing = boto3.client('pricing', region_name='us-east-1')

# Give all the choices in a series of print statements.
print("\nUS East (Ohio)	")
print("US East (N. Virginia)")
print("US West (N. California)")
print("US West (Oregon)")
    
# Ask for the user's choice.
desired_region = input("Input your desired region: ")

 
response = pricing.get_products(
     ServiceCode='AmazonEC2',
     Filters = [
         # TODO: let the user input filters 
         {'Type' :'TERM_MATCH', 'Field':'operatingSystem', 'Value':'Linux'              },
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


#collects keys and displays them
for key in entry.get('product', {}).get('attributes', {}):
    #prints key's
    print(key)


usr_input = input("from the list: ")
#iterates and prints keys associated with
print(entry.get('product', {}).get('attributes', {}).get(str(usr_input), {}))
#TODO: Add a way for users to attain pricing information



# store information in dictionary
product_attributes = {}

# for key, value in entry:
#     if key == usr_input:
#         product_attributes[key] = {}



for item in [entry]:
    if usr_input == 'sku':
        
    os = item.get("product").get("attributes").get("operatingSystem")
    product_attributes["os"] = os 

print(product_attributes)


# while usr_input != 'q':
#     #collects key information from the associated dict data
#     for key in entry.get('product', {}).get('attributes', {}):
#         #prints key's
#         print(key)
#     usr_input = input("from the list: ")
#     print(entry.get('product', {}).get('attributes', {}).get(str(usr_input), {}))
# print("Session ended.")


#TODO: If user inputs information into consol window have a program loop through the keys to determine if that value is in there based 
#on the first few letters, if no action is made after 5 seconds the program will execute and fetch data based on the first 