## Code quality-control with Python
### testsuites, paramaterized testcases, mocks and (test)code coverage
The aim of this project is to demonstrate a possible (and working) use and implementation of the unittest (standard) library. It can difficult to understand how things like mocks exactly work and how to set it up. Sometimes an examples is more clarifying than documentation.

Also it demonstrates a usecase of the `unitettest.TestSuite`. This can very usefull if you'd like to test the same testcase (`unittest.TestCase`) multiple times with different input parameters. To make this possible we've setup a TestBase (class unittest.TestCase) wich can accept a parameter. Then for the actual testcase we extend this TestBase class so that we can call it with parameters.

### Docker
To use the project with just enter the root folder and run `docker-compose up`. 

Your PYTHONPATH environment variable will be automatically set to the `/app` folder of the project (in the container) and needs no further manual actions. 


To enter to docker container and start running (python) command enter the following command: 
`docker exec -ti python_unittest_example_app_1 bash`

### App
The app (inside the 'app' folder) contains 2 elements. The first is the connector (to make http requests to another server) and the second is the logic. Here is determined when and where the application has to sent a request.

#### Workflow
The application will lookup the same product at several shops and determine wich shop offers the product for the lowest price. When it found that shop it will submit an order (by post request).

note: The url-structure and product-id is the same for each shop.

### Test strategy
To provide full (testcode)coverage for this application we not only needed to provide **unittests for the connector**, but also a test that covere the logic.py. This where we draw the line and no longer call it a 'unittest', since the `main()` hits different 'units'. Therefor we call this an **integration test**, that checks that the units interact correctly as expected.

### Run tests
You can execute the tests directly by python:

`python tests/unit_conncetor_test.py` 
`python tests/integration_test.py`


### Run coverage
To check (test)code coverage run the following commands"

```
coverage run app/tests/integration_test.py && 
coverage run -a app/tests/unit_connector_test.py &&
coverage report && coverage html
```

After running the commands above all unittests will been executed and analysed by coverage.py. Also an html report will have been created and can be found in the `app/report/htmlcov` directory.