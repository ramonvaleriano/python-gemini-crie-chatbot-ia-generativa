from service.google_genai import GoogleGenai


class SelecionarPersona:
    def selecionar_persona(self, message_user):
        prompt_do_sistema = """
                Assuma que você é um analisador de sentimentos de mensagem.

                1. Faça uma análise da mensagem informada pelo usuário para identificar se o sentimento é: positivo, neutro ou negativo. 
                2. Retorne apenas um dos três tipos de sentimentos informados como resposta.

                Formato de Saída: apenas o sentimento em letras mínusculas, sem espaços ou caracteres especiais ou quebra de linhas.

                # Exemplos

                Se a mensagem for: "Eu amo o MusiMart! Vocês são incríveis! 😍♻️"
                Saída: positivo

                Se a mensagem for: "Gostaria de saber mais sobre o horário de funcionamento da loja."
                Saída: neutro

                se a mensagem for: "Estou muito chateado com o atendimento que recebi. 😔"
                Saída: negativo
                """
        
        configuracao_modelo = {
            "temperature" : 0.1,
            "max_output_tokens" : 8192
        }

        llm_google = GoogleGenai(system_inproduction=prompt_do_sistema, generation_config=configuracao_modelo)
        response = llm_google.context_response(context=message_user)

        return response.text.strip().lower()


