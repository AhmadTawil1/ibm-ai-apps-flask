from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

quotes = [
    "Believe in yourself.",
    "Stay curious, keep learning.",
    "You were born to build cool stuff.",
    "Fall seven times, stand up eight.",
    "The best way to predict the future is to invent it."
]

@app.route("/")
def home():
    return render_template("index.html")  # serve the frontend

@app.route("/quote", methods=["GET"])
def get_quote():
    return jsonify({"quote": random.choice(quotes)})

if __name__ == "__main__":
    app.run(debug=True)
