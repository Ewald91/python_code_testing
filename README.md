## Demo unittest library: testsuites, paramaterized testcases and mocks
This project is to demonstrate a possible use and implementation of the mock method from the unittest (standard) library. It can difficult to understand how this works and how to setup different mocks. Sometimes an examples clears up more than the entire documentation.

Also it demonstrates a usecase of the `unitettest.TestSuite`. This can very usefull if you'd like to test the same testcase (`unittest.TestCase`) multiple times with different input parameters. To make this possible we've setup a TestBase (class unittest.TestCase) wich can accept a parameter. Then for the actual testcase we extend this TestBase class so that we can call it with parameters.

### Setup
This project doesn't really need to be set up since we're only demonstrating the use of the unittes standard library. So there is no

All you need to have is Python 3.6 (or above) installed. You can check this on your machine via the commandline with `python --version`.

Also to avoid import errors you need to PYTHONPATH environment variable to the `/app` folder. If you don't want to do this, then follow the (docker) instructions below.

### Docker
To use the project with just enter the root folder and run `docker-compose up`. 

Your PYTHONPATH environment variable will be automatically set to the `/app` folder of the project (in the container) and needs no further manual actions. 

### App
The app (inside the 'app' folder) contains out of 2 elements. The first is a connector class (to make http requests to another server) and the second is the logic it self. Here is determined when and where the application has to sent a request.

The application will lookup the same product at several (provided) shops and determine wich shop offers the lowest price. When it found the cheapest shop it will submit an order (by post request).

note: The url-structure and product-id is the same for each shop.

### Test strategy
To provide full (code)coverage for this application we not only needed to provide unittests for the connector, but also a test that covere the logic.py (main file). This where we draw the line and no longer call it a 'unittest', since the `main()` hit many different 'units'. Therefor we call this an integration (or component) test, that checks (eventhough mocked) that the units interact correctly as expected.

### Run tests
You can execute the tests directly by python:

`python tests/unit_conncetor_test.py` 
`python tests/integration_test.py`


### Run coverage
To check (test)code coverage run the following commands"

```
coverage run app/tests/integration_test.py && 
coverage html && 
coverage run app/tests/unit_connector_test.py
```

After running the commands above all unittests will been executed and analysed by coverage.py. Also an html report will have been created and can be found in the `app/report/htmlcov` directory.