# Implementation of testcases to test the API provided by fibservice

from fibservice import app

import unittest
import fibservice
import json

# A test class for the Global functions
class TestGlobalFunctions(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.client = app.test_client(self)

    # Test the fibonacci function
    def testfibonacci(self):
        # test for a single fibonacci series element
        expected = [0]
        response = fibservice.fibonacci(1)
        self.assertEqual(1, len(response))
        self.assertListEqual(expected, response)
        self.assertEqual(expected[0], response[0])

        # test scenario for size < 3 elements
        expected = [0, 1]
        response = fibservice.fibonacci(2)
        self.assertEqual(len(expected), len(response))
        self.assertListEqual(expected, response)
        for i in range(len(expected)):
            self.assertEqual(expected[i], response[i])

        # test scenario for size > 3 elements
        expected = [0, 1, 1, 2, 3, 5, 8]
        response = fibservice.fibonacci(7)
        self.assertEqual(len(expected), len(response))
        self.assertListEqual(expected, response)
        for i in range(len(expected)):
            self.assertEqual(expected[i], response[i])

    # Test the get_fibonacci function
    def testget_fibonacci(self):
        # Test if the correct fibonacci series is generated for a valid positive size
        expected = "{\n \"fibonacci\":[\n 0,\n 1,\n 1,\n 2\n ]\n}"
        response = self.client.get('/fibonacci/4', content_type='application/json')
        self.assertEqual(json.loads(expected), json.loads(response.data))

        # Test if the correct error message is generated if size is greater than 1500
        response = self.client.get('/fibonacci/1501', content_type='application/json')
        self.assertEqual(response.status_code, 400)
        assert 'Fibonacci sequence size must be less than 1,500.' in response.data

        # Test error message generated for invalid URL
        response = self.client.get('/fibonacciSeries/6', content_type='application/json')
        self.assertEqual(response.status_code, 404)
        self.assertIn('The requested URL was not found on the server.', response.data)

    def testget_negative_error(self):
        # Test if the correct error message is generated is size is a negative value
        response = self.client.get('/fibonacci/-4', content_type='application/json')
        self.assertEqual(response.status_code, 400)
        assert 'Fibonacci sequence size must be zero or a positive integer.' in response.data

# A test class for the RegexConverter class which contains only the constructor
class TestRegexConverter(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

# Run the tests
#if __name__ == '__main__':
    #unittest.main()

# Run all the tests in the TestGlobalFunctions class
suite = unittest.TestLoader().loadTestsFromTestCase(TestGlobalFunctions)
unittest.TextTestRunner(verbosity=2).run(suite)
