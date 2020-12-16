from connector import Connector
from unittest import mock
import logging
from app import logger

logger = logging.getLogger('logger')

def request_connector(shop, id, req='get'):
    """
    This method get's executed if logic states that a shop is the cheapest.
    """
    connector = Connector(shop)
    if req == 'get':
        response = connector.get(id)
        logger.info(f'performed GET-request to {shop}')
        return response.body['product']['Price']
    elif req == 'post':
        connector.post(id, {"action":"order"})
        logger.info(f'performed POST-request to {shop}')
        return f'Buy order has succesfully been placed at {shop}'
    else: 
        raise TypeError()

def get_prices(providers, id): 
    """
    This method has been created so that we can mock it inside the 
    unittests. This dictionary comprehension could also been used as 
    a variable within the main() method, but than it can't be mocked.
    """
    return {shop:request_connector(shop, id) for shop in providers} #no cover

def main(providers, id):
    """
    The main method collects all prices and submits an order
    for the shop with the lowest price available.
    """
    prices = get_prices(providers, id)
    request_connector(id, min(prices, key=prices.get), req='post')

if __name__ == '__main__':
    main(['bollie', 'coolbere', 'aliblabla'], 5)