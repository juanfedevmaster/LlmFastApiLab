import os
from dotenv import load_dotenv

load_dotenv()

MODEL_PATH = os.getenv("MODEL_PATH", "./models/mistral-7b-instruct.Q4_K_M.gguf")
CONTEXT_SIZE = int(os.getenv("CONTEXT_SIZE", 2048))
THREADS = int(os.getenv("THREADS", 4))

# Debug mode to skip model loading for testing
DEBUG_MODE = os.getenv("DEBUG_MODE", "False").lower() == "true"
