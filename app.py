from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Configura a chave da OpenAI a partir da variável de ambiente
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=["GET"])
def home():
    return "Bot WhatsApp GPT ativo!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()

    # Captura a mensagem recebida (ajuste conforme o formato da Opa Supíte, se necessário)
    user_message = data.get("message") or "Olá!"

    # Chamada à API da OpenAI
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um assistente simpático e prestativo."},
                {"role": "user", "content": user_message}
            ]
        )
        bot_reply = response.choices[0].message["content"].strip()
    except Exception as e:
        bot_reply = f"Erro ao processar a mensagem: {str(e)}"

    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
