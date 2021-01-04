"""
This module treats input text structured in a known format and extract the
relevant information.
"""
import delorean
from decimal import Decimal

# Suppose there is the following log (or logs)
log = '[2020-01-04T17:11:12.234529] - SALE - PRODUCT: 1256 - PRICE: $09.99'

# Split the log into its parts. Let's also ignore the SALE part
divide_it = log.split(' - ')
timestamp_string, _, product_string, price_string = divide_it

# Parse the timestamp into a datetime object
timestamp = delorean.parse(timestamp_string.strip('[]'))

# Parse the product_id into an integer
product_id = int(product_string.split(':')[-1])

# Parse the price into a Decimal type:
price = Decimal(price_string.split('$')[-1])

# Print all the values in native Python format
print((timestamp, product_id, price))
