from time import sleep

from utils.selecionar_persona import personas
from utils.helper import carrega, salva

from service.google_genai import GoogleGenai


def bot(prompt):
    maximo_tentativas = 1
    repeticao = 0

    contexto = carrega("data/musimart.txt")

    while True:
        try:
            personalidade = personas["negativo"]

            prompt_do_sistema = f"""
            # PERSONA
            Você é um chatbot de atendimento a clientes de um e-commerce. 
            Você não deve responder perguntas que não sejam dados do ecommerce informado!
            
            Você deve utilizar apenas dados que estejam dentro do 'contexto'

            # CONTEXTO
            {contexto}
            
            # PERSONALIDADE
            {personalidade}
            """

            configuracao_modelo = {"temperature": 0.1, "max_output_tokens": 8192}

            print("\nPreparando para envio para a GEMINI")
            llm_genai = GoogleGenai(
                system_inproduction=prompt_do_sistema,
                generation_config=configuracao_modelo,
            )
            resposta = llm_genai.context_response(context=prompt)

            return resposta.text

        except Exception as erro:
            repeticao += 1
            if repeticao >= maximo_tentativas:
                return "Erro no Gemini: %s" % erro

            sleep(50)
