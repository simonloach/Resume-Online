from flask import Flask
from jinja_parser import deployer
import os

app = Flask(__name__)

@app.route("/deploy")
def hello_world():
    deployer()
    return "<p>Deployed bruh!</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)