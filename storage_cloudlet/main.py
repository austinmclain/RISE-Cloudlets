from flask import Flask, request
from StorageServices import StorageServices
import shortuuid

app = Flask(__name__)

@app.route("/storageApi/", methods=['POST'])
def storeImage():
    uniqueId = shortuuid.uuid()
    s3 = StorageServices()
    return s3.storeImage(uniqueId, request.data)

@app.route("/storageApi/getImage", methods=['GET'])
def getImage():
    args = request.args
    key = args.get("key")
    return getImage(key)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081, debug=True)
