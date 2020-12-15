from connector import Connector
from unittest import mock
import logging
from datetime import datetime

logger = logging.getLogger() #provide '__name__' to getLogger for only logs from this module
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(funcName)s:%(message)s')

now = datetime.now()
file_handler = logging.FileHandler(f'logs/{now.strftime("%Y%m%d")}logic.log')
file_handler.setLevel(logging.WARNING)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

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
    prices = {}
    for shop in providers:
        prices[shop] = request_connector(shop, id)
        logger.info(f'called request_connector get-method')
    # print(prices)
    return prices
    # return {shop:request_connector(shop, id) for shop in providers} #no cover

def main(providers, id):
    """
    The main method collects all prices and submits an order
    for the shop with the lowest price available.
    """
    prices = get_prices(providers, id)
    request_connector(id, min(prices, key=prices.get), req='post')
    
    # logging.DEBUG(f'order place by POST-resquest for {min(prices, key=prices.get)}')


if __name__ == '__main__':
    main(['bollie', 'coolbere', 'aliblabla'], 5)