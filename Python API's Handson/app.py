from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "API Server is running "

@app.route("/hello", methods=["GET"])
def hello():
    return jsonify({
        "message": "Hello, welcome to APIs!",
        "status": "success"
    })

if __name__ == "__main__":
    app.run(debug=True)
