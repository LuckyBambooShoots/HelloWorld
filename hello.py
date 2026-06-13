from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return f"""
    <h1>🟡 Yellow World from AWS!</h1>
    <p>Current server time:</p>
    <h2>{datetime.now()}</h2>
    """

app.run(host="0.0.0.0", port=8080)