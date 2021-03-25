## Unit testing AWS services

To unit test (python) applications that interact with AWS infrastructure/service (via boto3 or botocore) you can use the 'moto' ('mock boto' == 'moto') library provided by AWS to fake/mock these services. 

You can easily install moto with `pip install moto` (or use `pip install -r requirements.txt` in the AWS directory of this project)

That simple apply a decorator (like: `@mock_s3`) to mock (read 'fake') the desired AWS service. This would bypass/avoid the 'no credentials' error. You would still have to setup service related resources like (in case of S3) a bucket. You shoudl use before-hooks where possible (setup methods of fixtures).

Attention: NOT ALL endpoints of all services are being covered by moto. Read there documentation for more information.