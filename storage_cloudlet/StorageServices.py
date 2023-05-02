import base64
import boto3

class StorageServices:
    # Note: This requires IAM configuration
    def storeImage(self, uniqueId, contents):
        # Prefix is encoded metadata about origin of image (project and instrument)
        image = f'prj-1_inst-1_{uniqueId}.png'
        try:
            s3 = boto3.resource('s3')
            s3.Object('rise-bucket123', image).put(Body=base64.b64decode(contents), Metadata={'project': '1', 'instrument': '1'})
            return {"status": 1, "msg": "image stored successfully", "data": image}
        except Exception as e:
            return {"status": 0, "msg": "error msg " + str(e)}
