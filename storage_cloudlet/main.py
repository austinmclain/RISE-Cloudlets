from flask import Flask, request
from StorageServices import StorageServices
import shortuuid

app = Flask(__name__)

@app.route("/storageApi/", methods=['POST'])
def storeImage():
    try:
        return StorageServices.storeImage(f'1-${shortuuid.uuid()}.png', request.data)
    except Exception as e:
        return e

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081, debug=True)
