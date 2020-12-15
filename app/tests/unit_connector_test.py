from connector import Connector
from unittest import TestCase, TestLoader, TestSuite, TextTestRunner
from unittest.mock import patch, call


class TestBase(TestCase):

    def __init__(self, methodName='runTest', param=None):
        super(TestBase, self).__init__(methodName)
        self.vendor = param
    
    @staticmethod
    def parametrize(testcase_class, param=None):
        testloader = TestLoader()
        testnames = testloader.getTestCaseNames(testcase_class)
        suite = TestSuite()
        for name in testnames:
            suite.addTest(testcase_class(name, param=param))
        return suite


class ConnectorTest(TestBase):

    def setUp(self):
        self.connector = Connector(self.vendor)
        self.response_get = {"product":
                                {
                                "Id":5,
                                "Price":4.89,
                                "Name":"Playdebiel"
                                }
                            }
        self.payload = {"action":"order"}

    def tearDown(self):
        print(f'Test for {self.vendor} is done!')

    @patch('connector.requests.get')
    def test_get(self, mocked_get):
        """
        This method covers the Connector instance making a correct get-request
        to the correctly (concatenated string) url.
        """
        mocked_get.return_value.status_code = 200
        mocked_get.return_value.ok = True
        mocked_get.return_value.body = self.response_get
                
        response = self.connector.get(5)

        mocked_get.assert_called_with(f'https://{self.vendor}.com/cadeaus/5')
        self.assertEqual(response.ok, True)
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.body)
        self.assertEqual(response.body, self.response_get)

    @patch('connector.requests.get')
    def test_get_not_ok(self, mocked_get):
        """
        This method covers the Connector instance making a incorrect get-request
        that returns a corresponding message.
        """
        mocked_get.return_value.status_code = 400
        mocked_get.return_value.ok = False
                
        response = self.connector.get(5)
        self.assertEqual(response.ok, False)
        self.assertIn(call.body('Bad response!'), response.mock_calls)

    @patch('connector.requests.post')
    def test_post(self, mocked_post):
        """
        This method covers the Connector instance making a correct post-request
        to the correctly (concatenated string) url.
        """
        mocked_post.return_value.status_code = 200
        mocked_post.return_value.ok = True
                
        response = self.connector.post(5, self.payload)

        mocked_post.assert_called_with(f'https://{self.vendor}.com/cadeaus/5', 
                                        data=self.payload)
        self.assertEqual(response.status_code, 200)

    @patch('connector.requests.post')
    def test_post_not_ok(self, mocked_post):
        """
        This method covers the Connector instance making a incorrect post-request
        that returns a corresponding message.
        """
        mocked_post.return_value.status_code = 400
        mocked_post.return_value.ok = False
                
        response = self.connector.post(5, self.payload)
        self.assertEqual(response.ok, False)
        self.assertIn(call.body('Bad response!'), response.mock_calls)
    

class AnotherTestCase(TestBase):

    def setUp(self):
        pass

    def test_1(self):
        """
        This method (is going to) show and prove that....
        """
        pass

    def test_2(self):
        """
        This method (is going to) show and prove that....
        """
        pass
    
if __name__ == '__main__':
    suite = TestSuite()
    # This testcase wil get executed multiple times for different inputs
    for vendor in ['bollie', 'aliblabla', 'coolbere']:
        suite.addTest(TestBase.parametrize(ConnectorTest, param=vendor))
    TextTestRunner(verbosity=2).run(suite)
