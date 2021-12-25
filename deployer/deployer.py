from flask import Flask
from jinja_parser import deployer
import os

app = Flask(__name__)

@app.route("/deploy")
def hello_world():
    repos = deployer()
    return "<p>Hello, World!</p>" + " ".join(os.listdir()) + str(repos)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)