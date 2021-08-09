# this main function imports all of the associated functions
import azure_pricing
import aws_noinput

prices = azure_pricing.get_azure_holding()
print(prices)

stock = aws_noinput.get_aws_products()
print(stock)