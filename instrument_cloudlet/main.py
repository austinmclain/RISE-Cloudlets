from flask import Flask
from connection import ssh_connection

app = Flask(__name__)

@app.route("/instrumentApi/command", methods=['GET'])
def command():
    try:
        ssh = ssh_connection()
        return ssh.command('ls')
    except Exception as e:
        return e
    
@app.route("/instrumentApi/download", methods=['GET'])
def download():
    try:
        ssh = ssh_connection()
        return ssh.download('experiment_1/Misc_pollen.jpg')
    except Exception as e:
        return e

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
