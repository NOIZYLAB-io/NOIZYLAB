
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/creative")
def creative():
    return "Creative Mode Ritual Triggered"

@app.route("/emotech")
def emotech():
    return "Emotional Tech Ritual Triggered"

@app.route("/emergency")
def emergency():
    return "Emergency Mode Ritual Triggered"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
