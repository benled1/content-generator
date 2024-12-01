from content_gen.storage.handlers.i_object_storage_handler import IObjectStorageHandler
from botocore.exceptions import ClientError
from dotenv import load_dotenv

import boto3
import os

class S3StorageHandler(IObjectStorageHandler):
    def __init__(self) -> None:
        load_dotenv()
        self.s3_session = boto3.Session(
            aws_access_key_id=os.getenv("S3_USER_ACCESS_KEY"),
            aws_secret_access_key=os.getenv("S3_USER_SECRET_ACCESS_KEY")
        )
        self.url_expiration = int(os.getenv("S3_PRESIGNED_URL_EXPIRATION", "3600"))

    def store_object(self, object_name: str, file_path: str, bucket: str) -> str:
        s3_client = self.s3_session.client('s3')
        try:
            s3_client.upload_file(file_path, bucket, object_name)
            return self._get_presigned_url(bucket, object_name)
        except ClientError as e:
            print(f"ERROR: exception when uploading: {e}")
            return None

    def _get_presigned_url(self, bucket: str, object_name: str) -> str:
        """Generate a presigned URL for the S3 object"""
        s3_client = self.s3_session.client('s3')
        try:
            url = s3_client.generate_presigned_url('get_object',
                Params={'Bucket': bucket, 'Key': object_name},
                ExpiresIn=self.url_expiration)
            return url
        except ClientError as e:
            print(f"ERROR: exception when generating presigned URL: {e}")
            return None