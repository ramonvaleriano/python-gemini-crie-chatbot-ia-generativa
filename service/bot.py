import google.generativeai as genai
from time import sleep

from core.settings import MODELO_ESCOLHIDO, GEMINI_API_KEY


genai.configure(api_key=GEMINI_API_KEY)


def bot(prompt):
    maximo_tentativas = 1
    repeticao = 0

    while True:
        try:
            prompt_do_sistema = """
            Você é um chatbot de atendimento a clientes de um e-commerce. 
            Você não deve responder perguntas que não sejam dados do ecommerce informado!
            """

            configuracao_modelo = {"temperature": 0.1, "max_output_tokens": 8192}
            print("\nPreparando para envio para a GEMINI")
            llm = genai.GenerativeModel(
                model_name=MODELO_ESCOLHIDO,
                system_instruction=prompt_do_sistema,
                generation_config=configuracao_modelo,
            )
            print("\nEnviando Pergunta")
            resposta = llm.generate_content(prompt)
            print("Resposta coletada")
            return resposta.text

        except Exception as erro:
            repeticao += 1
            if repeticao >= maximo_tentativas:
                return "Erro no Gemini: %s" % erro

            sleep(50)
