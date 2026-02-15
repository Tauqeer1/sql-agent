import os, sys
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import SQLDatabaseToolkit, create_sql_agent

# Load environment variables
load_dotenv()

def main():
    
    api_key = os.getenv("GOOGLE_API_KEY")
    db_uri = os.getenv("DB_URI")
    llm_provider = os.getenv("LLM_PROVIDER", "gemini").lower()
    
    if not db_uri:
        print("Error: Missing db connection string")
        sys.exit(1)
    # Database connection
    try:
        db = SQLDatabase.from_uri(db_uri)
        print(f"Connected to database dialect: {db.dialect}")
    except Exception as e:
        print(f"Error: Could not connect to database.\nDetails: {e}")
        sys.exit(1)

    # Model initialization
    try:
        if llm_provider == "ollama":
            print("Initializing Ollama...")
            llm = ChatOllama(model="llama3.2", temperature=0)
        elif llm_provider == "gemini":
            print("Initializing Gemini...")
            if not api_key:
                print("Error: Gemini api key required for model initialization.")
                sys.exit(1)
            llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", api_key=api_key)
        else:
            print(f"Error: Unknown LLM provider: {llm_provider}. Use ollama or gemini.")
            sys.exit(1)

        toolkit = SQLDatabaseToolkit(db=db, llm=llm)

        agent = create_sql_agent(
            llm=llm,
            toolkit=toolkit,
            verbose=True, 
            handle_parsing_errors=True
        )
    except Exception as e:
        print(f"Error: Could not initialize model.\nDetails: {e}")
        sys.exit(1)
    
    # Agent execution
    try:
        query = input("Enter your query: ")
        print(f"\nRunning query: {query} ...\n")
        response = agent.invoke(query)
        
        print("\nAgent response:\n")
        print(response["output"])
    except Exception as e:
        print(f"Error: Executing the agent query.\nDetails: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
