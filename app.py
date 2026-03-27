# Flask web server for the Data Science Chatbot
# - Serves the chat interface (index.html)
# - Handles AJAX POST requests to get chatbot responses
from flask import Flask, render_template, request, jsonify
from bot import get_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json["message"]
    reply = get_response(user_msg)
    return jsonify({"reply": reply})

app.run(debug=True)