# Hotel Bot Web API

A FastAPI-based web application that integrates with Llama models for hotel chatbot functionality.

## Project Structure

`
Hotel.BotWebApi/
 README.md
### Common Issues

1. **ModuleNotFoundError: No module named 'app.agent.base'**
   - The import should be from `app.agent.agente` not `app.agent.base`
   - Make sure all directories have `__init__.py` files

2. **Model file not found**
   - The model file (`*.gguf`) is not included in the repository and must be downloaded by each developer after cloning the repo.
   - See the section "Download the model (Required for production and development)" below for detailed instructions.
   - Place the downloaded file in the `models/` directory.
   - Update the `MODEL_PATH` in the `.env` file if needed.
   - For testing, set `DEBUG_MODE=True` in `.env` to skip model loading.

3. **Import errors with llama_cpp**
   - Ensure all system dependencies are installed
   - Try reinstalling: `pip uninstall llama-cpp-python && pip install llama-cpp-python==0.2.90`

4. **Port already in use**
   - Change port: `uvicorn app.main:app --port 8001`
   - Or kill existing process

5. **Module not found errors**
   - Ensure virtual environment is activated
   - Verify all dependencies are installed: `pip list`
   - Make sure all directories contain `__init__.py` files.txt
 app/
    main.py
    agent/
       agente.py
       tools/
    api/
       routes.py
    core/
       config.py
    models/
    services/
`

## Requirements

- Python 3.9+
- FastAPI
- Uvicorn
- llama-cpp-python
- python-dotenv

## Installation

### Local Development (Windows)

1. **Clone the repository**
   `Bash
   git clone <repository-url>
   cd Hotel.BotWebApi
   `

2. **Create a virtual environment**
   `Bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   # or
   source venv/bin/activate  # Linux/Mac
   `

3. **Install dependencies**
   `Bash
   pip install -r requirements.txt
   `

   **Note for Windows users**: If llama-cpp-python compilation fails, you may need to install Visual Studio Build Tools:
   - Download from: https://visualstudio.microsoft.com/visual-cpp-build-tools/
   - Select "C++ build tools" and "Windows SDK"
   - Restart and retry installation

4. **Set up environment variables**
   Create a .env file in the root directory:
   `env
   # Add your environment variables here
   DEBUG=True
   HOST=0.0.0.0
   PORT=8000
   MODEL_PATH=./models/mistral-7b-instruct.Q4_K_M.gguf
   CONTEXT_SIZE=2048
   THREADS=4
   DEBUG_MODE=True
   `


5. **Download the model (Required for production and development)**

   The model file (.gguf) is not included in the repository. Each developer must download it after cloning the repo.

   **Instructions:**

   - Create the models directory if it does not exist:
     ```sh
     mkdir models
     ```

   - Download the Mistral 7B Instruct GGUF model (example using curl):
     ```sh
     curl -L -o models/mistral-7b-instruct.Q4_K_M.gguf "https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/resolve/main/mistral-7b-instruct-v0.1.Q4_K_M.gguf"
     ```

     Or using wget:
     ```sh
     wget -O models/mistral-7b-instruct.Q4_K_M.gguf "https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/resolve/main/mistral-7b-instruct-v0.1.Q4_K_M.gguf"
     ```

     Or using PowerShell on Windows:
     ```powershell
     Invoke-WebRequest -Uri "https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/resolve/main/mistral-7b-instruct-v0.1.Q4_K_M.gguf" -OutFile "models/mistral-7b-instruct.Q4_K_M.gguf"
     ```

   - Update the `MODEL_PATH` in your `.env` file if needed:
     ```env
     MODEL_PATH=./models/mistral-7b-instruct.Q4_K_M.gguf
     ```

   **Note:** The `.gguf` model file is large and should not be committed to the repository.
   
   For development/testing, you can set `DEBUG_MODE=True` in your `.env` to skip model loading.

### Production Deployment (Linux)

The application is optimized for Linux deployment on platforms like:
- Azure Web Apps (Linux)
- AWS Elastic Beanstalk
- Google Cloud Run
- Heroku

#### Requirements Installation on Linux

`Bash
pip install -r requirements.txt
`

**Note**: Linux platforms typically include the necessary build tools (gcc, g++, make) for compiling llama-cpp-python automatically.

#### Docker Deployment

`dockerfile
FROM python:3.11-slim

# Install system dependencies (if needed)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
`

## Running the Application

### Development Mode

`Bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
`

### Production Mode

`Bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
`

The API will be available at: http://localhost:8000

### API Documentation

Once running, you can access:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Dependencies

### Core Dependencies

- **FastAPI (0.111.0)**: Modern, fast web framework for building APIs
- **Uvicorn[standard] (0.29.0)**: ASGI server implementation
- **python-dotenv (1.0.1)**: Load environment variables from .env file
- **llama-cpp-python (0.2.90)**: Python bindings for llama.cpp

### Additional Dependencies (Auto-installed)

- **Starlette**: ASGI framework (FastAPI dependency)
- **Pydantic**: Data validation using Python type annotations
- **Jinja2**: Template engine
- **Python-multipart**: For handling file uploads
- **Email-validator**: Email validation
- **UJson**: Ultra fast JSON encoder and decoder
- **OrJson**: Fast JSON library

## Troubleshooting

### llama-cpp-python Installation Issues

#### Windows
If installation fails on Windows:
1. Install Visual Studio Build Tools
2. Or use WSL (Windows Subsystem for Linux)
3. Or develop on Linux/Docker

#### Linux
Usually works out of the box. If issues occur:
`Bash
# Install build tools
sudo apt-get update
sudo apt-get install build-essential

# Then retry
pip install llama-cpp-python==0.2.90
`

### Common Issues

1. **Import errors with llama_cpp**
   - Ensure all system dependencies are installed
   - Try reinstalling: pip uninstall llama-cpp-python && pip install llama-cpp-python==0.2.90

2. **Port already in use**
   - Change port: uvicorn app.main:app --port 8001
   - Or kill existing process

3. **Module not found errors**
   - Ensure virtual environment is activated
   - Verify all dependencies are installed: pip list

## Development

### Project Structure Explained

- **app/main.py**: Main application entry point
- **app/agent/**: AI agent logic and tools
- **app/api/**: API routes and endpoints
- **app/core/**: Core configuration and settings
- **app/models/**: Data models and schemas
- **app/services/**: Business logic services

### Adding New Features

1. Create new routes in pp/api/
2. Add models in pp/models/
3. Implement business logic in pp/services/
4. Update agent tools if needed in pp/agent/tools/

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## Support

For issues and questions:
- Create an issue in the repository
- Check the troubleshooting section above
- Review FastAPI documentation: https://fastapi.tiangolo.com/
