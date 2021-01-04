"""
This module contains a price log object that helps to  aggregate some
known log structure.
"""
import delorean
from decimal import Decimal

class PriceLog:
    def __init__(self, timestamp, product_id, price):
        self.timestamp = timestamp
        self.product_id = product_id
        self.price = price

    def __repr__(self):
        return '<PriceLog ({}, {}, {})>'.format(self.timestamp,
                                                self.product_id,
                                                self.price)

    @classmethod
    def parse(cls, text_log):
        """
        Parse from a text log with the format

        [<timestamp] - SALE - PRODUCT: <product id> - PRICE: $<price>

        to a PriceLog object.
        """
        divide_it = text_log.split(' - ')
        timestamp_string, _, product_string, price_string = divide_it

        timestamp = delorean.parse(timestamp_string.strip('[]'))
        product_id = int(product_string.split(':')[-1])
        price = Decimal(price_string.split('$')[-1])

        return cls(timestamp=timestamp,
                   product_id=product_id,
                   price=price)
