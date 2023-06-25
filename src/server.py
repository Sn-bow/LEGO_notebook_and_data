from flask import Flask, jsonify, render_template, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return "start"


if __name__ == "__main__":
    app.run(debug=True, port=8080, host="0.0.0.0")