from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json["message"]
    try:
        response = requests.post("http://localhost:11434/api/generate", json={
            "model": "llama3.2",
            "prompt": user_input,
            "stream": False,
            "options": {"num_predict": 1000}
        })
        reply = response.json()["response"]
    except Exception as e:
        reply = f"Error: {e}"
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)

