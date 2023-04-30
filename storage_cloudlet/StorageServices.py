import base64
import boto3

class StorageServices:
    def __downloadImage(self, localPath, contents):
        new_image = open(localPath, 'wb')
        new_image.write(base64.b64decode(contents))
        new_image.close()
    
    # Note: This requires IAM configuration
    def storeImage(self, localPath, contents):
        try:
            self.__downloadImage(localPath, contents)
            client = boto3.client('s3', region_name='us-east-1')
            client.upload_file(localPath, 'rise-bucket123', localPath)
            return {"status": 1, "msg": "image stored successfully", "data": localPath}
        except Exception as e:
            return {"status": 0, "msg": "error msg " + str(e)}
