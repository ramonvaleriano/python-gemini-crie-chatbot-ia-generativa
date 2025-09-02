import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", None)
MODELO_ESCOLHIDO = os.getenv("MODELO_ESCOLHIDO", None)

MODELO_GEMMA = os.getenv("MODELO_GEMMA", None)
MODELO_FLASH_LEARN = os.getenv("MODELO_FLASH_LEARN", None)

