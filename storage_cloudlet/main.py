from flask import Flask, request
from StorageServices import StorageServices
import shortuuid

app = Flask(__name__)

@app.route("/storageApi/", methods=['POST'])
def storeImage():
    uniqueId = shortuuid.uuid()
    s3 = StorageServices()
    return s3.storeImage(uniqueId, request.data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
