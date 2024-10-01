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

    def store_object(self, object_name: str, file_path: str, bucket: str) -> bool:
        """
        call the boto3 method here
        """

        s3_client = self.s3_session.client('s3')
        try:
            response = s3_client.upload_file(file_path, bucket, object_name)
        except ClientError as e:
            print(f"ERROR: exception when uploading: {e}")
            return False
        return True