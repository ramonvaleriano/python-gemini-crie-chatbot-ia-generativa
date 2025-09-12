import google.generativeai as genai
from core.settings import MODELO_ESCOLHIDO, GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)


class GoogleGenai:
    def __init__(self, system_inproduction=None, generation_config=None, history=list()):
        self.system_inproduction = system_inproduction
        self.__modelo_escolhido = MODELO_ESCOLHIDO
        self.__generation_config = generation_config
        self.llm = self.__set_generative_model()
        self.__history = history

    def __set_generative_model(self):
        print("\n")
        if self.__generation_config:
            print("Configurando Modelo com Congfiguração Generativa")
            return genai.GenerativeModel(
                model_name=self.__modelo_escolhido,
                system_instruction=self.system_inproduction,
                generation_config=self.__generation_config,
            )

        print("Configurando Modelo sem Configuração Generativa")
        return genai.GenerativeModel(
            model_name=self.__modelo_escolhido,
            system_instruction=self.system_inproduction,
        )

    def context_response(self, context):
        print("\n")
        print("Enviando pergunta")
        response = self.llm.generate_content(context)
        print("Resposta coletada")
        return response
    
    def chatbot(self):
        chatbot = self.llm.start_chat(history=self.__history)

        return chatbot

class ImageManager:
    def generating_gemini_image(self, path_image):
        temporary_file = genai.upload_file(
            path=path_image,
            display_name="Imagem Enviada"
        )

        print(f"Imagem enviada: {temporary_file.uri}")

        return temporary_file