# this main function imports all of the associated functions
import azure_pricing
import aws_noinput

def unit_price_compare(aws, azure):
    if float(aws.get('unitPrice')) > float(azure.get('unitPrice')):
        return azure
    else:
        return aws

azure_item = azure_pricing.get_azure_holding()
#prints the price of the dict
print(azure_item.get('unitPrice'))

aws_item = aws_noinput.get_aws_products()
print(aws_item.get('unitPrice'))

#doesn't matter what data we are working with 
#comparing prices here
print(unit_price_compare(aws_item, azure_item))