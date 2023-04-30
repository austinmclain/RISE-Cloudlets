from flask import Flask, request
from InstrumentServices import InstrumentServices
import requests

app = Flask(__name__)

@app.route("/instrumentApi/runExperiment", methods=['GET'])
def runExperiment():
    try:
        sem = InstrumentServices()
        return sem.runExperiment()
    except Exception as e:
        return e
    
@app.route("/instrumentApi/saveImage", methods=['POST'])
def saveImage():
    try:
        id = request.form['id']
        sem = InstrumentServices()
        return sem.saveImage(id)
    except Exception as e:
        return e

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
