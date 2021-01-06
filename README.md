# Quality control- and assurance on Python code
In this project we'll show examples of components that make a great 

This project demos following component:
- unittests
- integrationtests
- mocks
- coverage
- linting (static code analysis)


## Target/demo application

### Installation - Docker
To use the project with just enter the root folder and run `docker-compose up`. 

Inside the containe app-container the PYTHONPATH will get set to the `/app` folder of the project and needs no further manual actions. 

To enter to docker container and start running (python) command enter the following command: 
`docker exec -ti python_code_testing_app_1 bash`

### App
The app (inside the 'app' folder) contains 2 elements. The first is the connector (to make http requests to another server) and the second is the logic. Here is determined when and where the application has to sent a request.

#### Workflow
The application will lookup the same product at several shops and determine wich shop offers the product for the lowest price. When it found that shop it will submit an order (by post request).

note: The url-structure and product-id is the same for each shop.

### Test strategy
To provide full (testcode)coverage for this application we not only needed to provide **unittests for the connector**, but also a test that covere the logic.py. This where we draw the line and no longer call it a 'unittest', since the `main()` hits different 'units'. Therefor we call this an **integration test**, that checks that the units interact correctly as expected.

### Unittests
You can execute the tests directly by python:

`python tests/unit_conncetor_test.py` 


### Integrationtests
You can execute the tests directly by python:

`python tests/integration_test.py`


### Coverage
To check (test)code coverage run the following command(s)"

```
coverage run app/tests/integration_test.py && 
coverage run -a app/tests/unit_connector_test.py &&
coverage html
```

After running the commands above all unittests will been executed and analysed by coverage.py. Also an html report will have been created and can be found in the `app/report/htmlcov` directory.