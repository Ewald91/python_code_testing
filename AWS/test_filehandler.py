import boto3
from moto import mock_s3
from filehandler import S3FileHandler

@mock_s3
def test_upload_s3_file():
    s3_client = boto3.client("s3")
    s3_client.create_bucket(Bucket="my_bucket")

    s3_handler = S3FileHandler()
    s3_handler.upload_s3_file('target_file.txt')

    objects = s3_client.list_objects(Bucket="my_bucket")
    assert objects['Contents'][0]['Key'] == 'target_file.txt'