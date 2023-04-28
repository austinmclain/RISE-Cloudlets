from flask import Flask
from InstrumentServices import InstrumentServices
import requests

app = Flask(__name__)

@app.route("/instrumentApi/runCommand", methods=['GET'])
def runCommand():
    try:
        services = InstrumentServices()
        return services.runCommand('ls')
    except Exception as e:
        return e
    
@app.route("/instrumentApi/uploadImage", methods=['GET'])
def uploadImage():
    try:
        remotePath = 'experiment_1/Misc_pollen.jpg'
        localPath = 'image_1.png'
        services = InstrumentServices()
        return services.uploadImage(remotePath, localPath)
    except Exception as e:
        return e

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
