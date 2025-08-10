import os
from llama_cpp import Llama
from app.core.config import MODEL_PATH, CONTEXT_SIZE, THREADS, DEBUG_MODE

# Initialize the model
llm = None

def initialize_model():
    global llm
    if DEBUG_MODE:
        print("DEBUG MODE: Model loading skipped")
        return
    
    if not os.path.exists(MODEL_PATH):
        print(f"Warning: Model file not found at {MODEL_PATH}")
        print("Please download a GGUF model and place it in the models directory")
        return
    
    try:
        print(f"Loading model from {MODEL_PATH}...")
        llm = Llama(
            model_path=MODEL_PATH,
            n_ctx=CONTEXT_SIZE,
            n_threads=THREADS
        )
        print("Model loaded successfully!")
    except Exception as e:
        print(f"Error loading model: {e}")

def generate_answer(prompt: str, max_tokens: int = 150) -> str:
    if llm is None:
        return "Model not loaded. Please check model configuration and ensure the model file exists."
    
    try:
        result = llm(prompt, max_tokens=max_tokens)
        return result["choices"][0]["text"].strip()
    except Exception as e:
        return f"Error generating response: {str(e)}"

# Initialize model on import
initialize_model()