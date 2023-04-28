from flask import Flask, request
from StorageServices import StorageServices

app = Flask(__name__)

@app.route("/storageApi/receiveImage", methods=['POST'])
def receiveImage():
    services = StorageServices()
    return services.storeImage('image_1.png', request.data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081, debug=True)
