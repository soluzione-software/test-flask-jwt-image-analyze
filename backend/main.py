from flask import Flask, request, jsonify
from auth import authenticate, token_required
from emotion import analyze_emotion

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Welcome to the Emotion Analysis API"}), 200
@app.route("/login", methods=["POST"])
def login():
    auth_data = request.get_json()
    token = authenticate(auth_data)
    if token:
        return jsonify({"token": token})
    return jsonify({"message": "Invalid credentials"}), 401

@app.route("/analyze", methods=["POST"])
@token_required
def analyze():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400
    image_file = request.files['image']
    result = analyze_emotion(image_file)
    return jsonify(result)

if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host="0.0.0.0", port=5000, debug=True)

