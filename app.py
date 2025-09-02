from flask import Flask,render_template, request, Response
from flask_cors import CORS

from service.bot import bot

app = Flask(__name__)
CORS(app)
app.secret_key = 'alura'

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
