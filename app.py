import os
import uuid
from flask import Flask,render_template, request, Response
from flask_cors import CORS

from service.bot import bot

app = Flask(__name__)
CORS(app)
app.secret_key = 'alura'

caminho_imagem_enviada = None
UPLOAD_FOLDER = "imagens_temporarias"

@app.route("/upload_imagem", methods=["POST"])
def upload_imagem():
    global caminho_imagem_enviada

    if "imagem" in request.files:
        imagem_enviada = request.files["imagem"]
        nome_arquivo = str(uuid.uuid4()) + os.path.splitext(imagem_enviada.filename)[1]
        caminho_arquivo = os.path.join(UPLOAD_FOLDER, nome_arquivo)
        imagem_enviada.save(caminho_arquivo)
        return "Imagem enviada com sucesso", 200
    return "Nenhum arquivo enviado", 400


@app.route("/chat", methods=["POST"])
def chat():
    prompt = request.json["msg"]
    resposta = bot(prompt)
    return resposta

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
