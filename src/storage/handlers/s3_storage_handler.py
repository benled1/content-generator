from i_storage_handler import IStorageHandler


class S3StorageHandler(IStorageHandler):

    def store_object(self, object_path: str):
        """
        call the boto3 method here
        """
        pass