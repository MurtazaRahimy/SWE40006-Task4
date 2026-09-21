import os, socket
from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def index():
    return (f"<h1>{os.getenv('APP_TITLE', 'Task 4.3')}</h1>"
            f"<p>Environment: {os.getenv('APP_ENV', 'dev')}</p>"
            f"<p>Container: {socket.gethostname()}</p>")

@app.route("/health")
def health():
    return jsonify(status="ok")
