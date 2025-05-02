from flask import Flask, request, jsonify
import openai
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    message = data.get("message")

    if not message:
        return jsonify({"error": "Mensagem não encontrada"}), 400

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message}]
    )

    reply = response["choices"][0]["message"]["content"]
    return jsonify({"reply": reply})