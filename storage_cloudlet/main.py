from flask import Flask

app = Flask(__name__)

@app.route("/storageApi", methods=['GET'])
def hello_world():
    return "<p>Storage Cloudlet</p>\n"

# @app.route("/save_image", methods=['POST'])
#     Get image metadata from request
#     Send to S3

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
