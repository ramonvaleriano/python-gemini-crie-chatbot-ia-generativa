from time import sleep

from utils.selecionar_persona import personas
from utils.helper import carrega, salva

from service.google_genai import GoogleGenai
from service.selecionar_persona import SelecionarPersona


contexto = carrega("data/musimart.txt")

def cria_chatbot():
    personalidade = "neutro"

    prompt_do_sistema = f"""
    # PERSONA
    Você é um chatbot de atendimento a clientes de um e-commerce. 
    Você não deve responder perguntas que não sejam dados do ecommerce informado!
    
    Você deve utilizar apenas dados que estejam dentro do 'contexto'

    # CONTEXTO
    {contexto}
    
    # PERSONALIDADE
    {personalidade}

    # Histórico
    Acesse sempre o histórico de mensagens, e recupere informações ditas anteriormente.
    """

    configuracao_modelo = {"temperature": 0.1, "max_output_tokens": 8192}

    print("\nPreparando para envio para a GEMINI")
    llm_genai = GoogleGenai(
        system_inproduction=prompt_do_sistema,
        generation_config=configuracao_modelo,
    )
    
    chatbot = llm_genai.llm.start_chat(history=[])

    return chatbot

chatbot = cria_chatbot()

def bot(prompt):
    maximo_tentativas = 1
    repeticao = 0

    while True:
        try:
            sentimento = SelecionarPersona().selecionar_persona(message_user=prompt)
            print(f"Sentimento gerado {sentimento}")
            personalidade = personas[sentimento]

            mwensagem_usuario = f"""
            Considere está personalidade para responder a mensagem: {personalidade}

            responda a seguinte mensagem, sempre lembrando do histórico:
            {prompt}
            """

            response = chatbot.send_message(mwensagem_usuario)

            return response.text

        except Exception as erro:
            repeticao += 1
            if repeticao >= maximo_tentativas:
                return "Erro no Gemini: %s" % erro

            sleep(50)
