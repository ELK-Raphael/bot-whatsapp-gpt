
from flask import Flask, request, jsonify
import openai
import os
import requests

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")  # A chave virá da variável de ambiente no Render

@app.route("/webhook", methods=["POST"])
def whatsapp_webhook():
    data = request.get_json()
    mensagem = data.get("mensagem", "")
    numero = data.get("numero", "")

    # Enviando a mensagem para o ChatGPT
    resposta = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[
            {
                "role": "system",
                "content": "Você é um atendente virtual da empresa VelozNet, um provedor de internet. Sempre responda com simpatia, peça o CEP antes de listar planos, e siga as políticas da empresa."
            },
            {"role": "user", "content": mensagem}
        ]
    )

    resposta_texto = resposta["choices"][0]["message"]["content"]

    # Aqui você enviaria de volta a resposta para o número no WhatsApp
    # Substitua pela sua própria URL da API do WhatsApp
    requests.post("https://sua-api-de-whatsapp.com/enviar", json={
        "numero": numero,
        "mensagem": resposta_texto
    })

    return jsonify({"resposta": resposta_texto})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
