# Intelligent SQL Agent 🦜🔗

This project is an intelligent SQL Agent that allows you to interact with your relational database using natural language. Built with Python and LangChain, it translates plain English questions into SQL queries, executes them against your database, and returns the answers in a human-readable format.

It supports switching between cloud-based models (Google Gemini) and local models (Ollama) via simple configuration.

## 🚀 Features

- **Natural Language Interface**: Ask questions like _"Who are the top 5 spending customers?"_ instead of writing complex SQL joins.
- **Dual LLM Support**:
  - ☁️ **Google Gemini** (`gemini-2.5-flash`) for high-speed, cloud-based reasoning.
  - 🏠 **Ollama** (`llama3.2`) for local, privacy-focused execution.
- **Secure**: Uses environment variables for API keys and database credentials.
- **Robust Error Handling**: Provides clear feedback for database connection failures or API errors.

## 📋 Prerequisites

- Python 3.10+
- MySQL Database (or any SQLAlchemy-supported database)
- **For Local LLM**: [Ollama](https://ollama.com/) installed and running.
- **For Cloud LLM**: A [Google AI Studio](https://aistudio.google.com/) API Key.

## 🛠️ Installation

1.  **Clone the repository**

    ```bash
    git clone https://github.com/Tauqeer1/sql-agent.git
    cd sql-agent
    ```

2.  **Set up a Virtual Environment**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

## ⚙️ Configuration

1.  Create a `.env` file in the root directory:

    ```bash
    touch .env
    ```

2.  Add your configuration details to `.env`:

    ```env
    # Database Connection (Required)
    # Format: dialect+driver://username:password@host:port/database
    DB_URI=mysql+pymysql://root:password@localhost:3306/Chinook

    # LLM Provider Selection
    # Options: 'gemini' or 'ollama'
    LLM_PROVIDER=gemini

    # Required only if using 'gemini'
    GOOGLE_API_KEY=your_google_api_key_here
    ```

## 🏃 Usage

1.  **Ensure your database is running.**
2.  **If using Ollama**, make sure the model is pulled:
    ```bash
    ollama pull llama3.2
    ```
3.  **Run the agent:**

    ```bash
    python3 main.py
    ```

4.  **Enter your question** when prompted:
    ```text
    Connected to database dialect: mysql
    Initializing Gemini...
    Enter your query: How many tracks are there in the playlist "Music"?
    ```

## 📄 Project Structure

- `main.py`: The core application logic, setup, and execution loop.
- `.env`: Configuration file for secrets (git-ignored).
- `requirements.txt`: Python dependencies.

## 🤝 Contributing

Feel free to submit issues or pull requests if you have ideas for improvements!
