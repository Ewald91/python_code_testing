#filehandler.py
import os
import boto3


class S3FileHandler:

    def __init__(self):
        self.s3_session = boto3.session.Session()
        self.s3_client = self.s3_session.client('s3')
        self.bucket = 'my_bucket'
        self.file_path = os.path.dirname(os.path.realpath(__file__))

    def upload_s3_file(self, file_name):
        path_to_file = os.path.join(self.file_path, file_name)

        self.s3_client.upload_file(
            path_to_file,
            self.bucket,
            file_name
        )
