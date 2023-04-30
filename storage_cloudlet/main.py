from flask import Flask, request
from StorageServices import StorageServices
import shortuuid

app = Flask(__name__)

@app.route("/storageApi/", methods=['POST'])
def storeImage():
    return StorageServices.storeImage(f'1-{shortuuid.uuid()}.png', request.data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081, debug=True)
