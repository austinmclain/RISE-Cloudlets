from flask import Flask
from connection import ssh_connection

app = Flask(__name__)

@app.route("/cloudletApi", methods=['GET'])
def cloudletApi():
    try:
        return ssh_connection('ls')
    except Exception as e:
        return e

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
