fibservice.py
	This file contains the implementation of the fibservice - a service used to generate 
	the fibonacci series of n elements(where n is less than or equal to 1500)
      
	To run this service, type the following command:
		python fibservice.py

fibserviceTest.py
	This file contains the tests to test the functionality of all the global functions in 
	fibservice.py

	To run the tests, type the following at the command:
		python fibserviceTest.py
	
	3 tests will be run and the following output generated if all the tests pass.

		testfibonacci (__main__.TestGlobalFunctions) ... ok
		testget_fibonacci (__main__.TestGlobalFunctions) ... ok
		testget_negative_error (__main__.TestGlobalFunctions) ... ok

		----------------------------------------------------------------------
		Ran 3 tests in 0.030s

		OK

ServiceAPITest.py
	This file contains the tests to test the API exposed by the fibservice.

	To run the tests, first start the service with the following command:
		python fibservice.py

	In another command window, run the tests using:
		python ServiceAPITest.py

	The following messages appear on the command window:
		Tests Started
		Finished Running All The Tests

	You will also see the following messages for each service request in the service window:
		127.0.0.1 - - [21/Sep/2013 21:32:28] "GET /fibonacciSeries/5 HTTP/1.1" 404 -
		127.0.0.1 - - [21/Sep/2013 21:32:29] "GET /fibonacci/5 HTTP/1.1" 200 -
		127.0.0.1 - - [21/Sep/2013 21:32:30] "GET /fibonacci/1501 HTTP/1.1" 400 -
		127.0.0.1 - - [21/Sep/2013 21:32:31] "GET /fibonacci/-4 HTTP/1.1" 400 -
		127.0.0.1 - - [21/Sep/2013 21:32:32] "GET /fibonacci/2 HTTP/1.1" 200 -
		127.0.0.1 - - [21/Sep/2013 21:32:33] "GET /fibonacci/0 HTTP/1.1" 200 -
		127.0.0.1 - - [21/Sep/2013 21:32:34] "POST /fibonacci/2 HTTP/1.1" 405 -