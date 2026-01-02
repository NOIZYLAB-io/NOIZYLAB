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

# To run the app in kiosk mode on Google Chrome, use the following command:
# /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome \
#   --kiosk "http://localhost:8080" \
#   --start-fullscreen
