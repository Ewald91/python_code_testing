from logic import main, request_connector
import logic
from connector import Connector
from unittest.mock import patch
import unittest
from datetime import datetime


class IntegrationTest(unittest.TestCase):

    def setUp(self):
        self.response_body = {"product":
                            {
                            "Id":id,
                            "Price": 12.34,
                            "Name":"Playdebiel"
                            }
                        }

    def tearDown(self):
        pass

    @patch('connector.requests.post')
    def test_request_connector_post(self, mocked_post):
        """
        This test shows that the request_connector method can recieve a call 
        and initiate a Connector instance to make a post request to the 
        correctly concatenated url string and recieving the right respo.
        """
        mocked_post.return_value.status_code = 200
        mocked_post.return_value.ok = True

        with self.assertLogs() as logs:
            response = request_connector('coolbere', 5, req='post')
        self.assertEqual(len(logs.records),2)
        self.assertEqual(logs.output, 
        ['INFO:connector:POST request (for coolbere) succesfully made', 
        'INFO:logic:performed POST-request to coolbere'])
        self.assertEqual(logs.records[0].getMessage(),"POST request (for coolbere) succesfully made")
        
        print(f'logs.output: {logs.output}')
        print(f'logs.records: {logs.records}')

        mocked_post.assert_called_with('https://coolbere.com/cadeaus/5', 
                                        data={'action': 'order'})
        self.assertEqual(response, 'Buy order has succesfully been placed at coolbere')
    
    @patch('connector.requests.get')
    def test_request_connector_get(self, mocked_get):
        """
        This test shows that the application can make a correct
        get request to the correctly concatenated url string.
        """
        mocked_get.return_value.status_code = 200
        mocked_get.return_value.ok = True
        mocked_get.return_value.body = self.response_body

        response = request_connector('coolbere', 5)

        mocked_get.assert_called_with('https://coolbere.com/cadeaus/5')
        self.assertEqual(response, 12.34)

    @patch('logic.request_connector') # mocking this method to assert that it's called (with correct parameters)
    @patch('logic.get_prices')
    def test_main(self, mocked_prices, mocked_request_connector):
        """
        test_main is assuring that the shop with the lowest price get's 
        called with a post-request to place an order.
        """
        mocked_prices.return_value = {'bollie':12.34, 'coolbere':2.34, 'aliblabla':34.56}
        

        results = main(['bollie', 'coolbere', 'aliblabla'], 5)


        mocked_request_connector.assert_called_with(5, 'coolbere', req='post')
    
    def test_connector_wrong(self):
        """
        This test shows that when the request_connector method is called
        upon with an invalid keyword argument a TypeError will get raised.
        """
        with self.assertRaises(TypeError):
            request_connector('myShop', 1, req='unknowValue')
               
if __name__ == '__main__':
    unittest.main()