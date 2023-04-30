import base64
import boto3

class StorageServices:
    # Note: This requires IAM configuration
    def storeImage(self, uniqueId, contents):
        image = f'1-{uniqueId}.png'
        try:
            s3 = boto3.resource('s3')
            s3.Object('rise-bucket123', image).put(Body=contents, Metadata={'instrument': 1, 'project': 1})
            return {"status": 1, "msg": "image stored successfully", "data": image}
        except Exception as e:
            return {"status": 0, "msg": "error msg " + str(e)}
