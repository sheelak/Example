#-------------------------------------------------------------------------------
# Name:        TestFibService
#
# Created:     21/09/2013
#-------------------------------------------------------------------------------

import requests
import json

class TestFibServiceURL():

    def testValidURL(self):
        # Test the response for a valid URL and size limit
        url = 'http://localhost:5000/fibonacci/5'
        fibseries5 = '{\n \"fibonacci\": [\n 0,\n 1,\n 1,\n 2,\n 3\n ]\n}'
        resp = requests.get(url)
        assert resp.status_code == 200
        assert resp.url == url
        assert json.loads(resp.content) == json.loads(fibseries5)

    def testInvalidURL(self):
        # Test the response for an invalid URL
        url = 'http://localhost:5000/fibonacciSeries/5'
        invalidURL = 'The requested URL was not found on the server.'
        resp = requests.get(url)
        assert resp.status_code == 404
        assert invalidURL in resp.content

class TestFibServiceGet:

    def testInvalidSize(self):
        # Test the response for incorrect size limit
        url = 'http://localhost:5000/fibonacci/1501'
        invalidSize = 'Fibonacci sequence size must be less than 1,500.'
        resp = requests.get(url)
        assert resp.status_code == 400
        assert invalidSize in resp.content

    def testNegativeSize(self):
        # Test the response for negative size
        url = 'http://localhost:5000/fibonacci/-4'
        negativeSize = 'Fibonacci sequence size must be zero or a positive integer.'
        resp = requests.get(url)
        assert resp.status_code == 400
        assert negativeSize in resp.content

    def testZeroSize(self):
        # Test the response for zero elements
        url = 'http://localhost:5000/fibonacci/0'
        fibseries = '{\n \"fibonacci\": []\n}'
        resp = requests.get(url)
        assert resp.status_code == 200
        assert resp.url == url
        assert json.loads(resp.content) == json.loads(fibseries)

    def testSizeBelowThree(self):
        # Test the response for less than 3 elements
        url = 'http://localhost:5000/fibonacci/2'
        fibseries2 = '{\n \"fibonacci\": [\n 0,\n 1\n ]\n}'
        resp = requests.get(url)
        assert resp.status_code == 200
        assert resp.url == url
        assert json.loads(resp.content) == json.loads(fibseries2)

class TestFibServicePost:

    def TestPostMethod(self):
        # Test the post method
        # Since the service does not support any storage or update
        # of persistent information this test is invalid.
        body = json.dumps('{\n \"fibonacci\": [\n 0,\n 1\n ]\n}')
        methodNotAllowed = 'Method Not Allowed'
        postResp = requests.post("http://localhost:5000/fibonacci/2", data=body)
        assert postResp.status_code == 405
        assert methodNotAllowed in postResp.content

# Run the tests in each class
print "Tests Started"
test1 = TestFibServiceURL()
test1.testInvalidURL()
test1.testValidURL()

test2 = TestFibServiceGet()
test2.testInvalidSize()
test2.testNegativeSize()
test2.testSizeBelowThree()
test2.testZeroSize()

test3 = TestFibServicePost()
test3.TestPostMethod()
print "Finished Running All The Tests"

