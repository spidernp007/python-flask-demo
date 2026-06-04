from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
    <title>OpenShift GitOps Demo</title>
    </head>
    <body>

    <h1>OpenShift GitOps Flask Demo</h1>

    <br>

    <button onclick="window.location.href='/red'">
    Red
    </button>

    <button onclick="window.location.href='/green'">
    Green
    </button>

    <button onclick="window.location.href='/blue'">
    Blue
    </button>

    </body>
    </html>
    """

@app.route("/red")
def red():
    return "<h1 style='color:red'>RED PAGE</h1>"

@app.route("/green")
def green():
    return "<h1 style='color:green'>GREEN PAGE</h1>"

@app.route("/blue")
def blue():
    return "<h1 style='color:blue'>BLUE PAGE</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
