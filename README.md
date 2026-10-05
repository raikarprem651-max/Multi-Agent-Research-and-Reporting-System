# ResearchMind · AI Research Agent 🔬

ResearchMind is a Streamlit-based multi-agent system powered by `langchain` and `mistralai`. It automates the process of researching any topic across the web, writing structured reports, and critically reviewing those findings. 

## Features
- **Search Agent:** Conducts web search to discover relevant information.
- **Reader Agent:** Scrapes and processes findings from websites.
- **Writer Chain:** Synthesizes the gathered research into a structured, professional report (with Key Findings and Sources).
- **Critic Chain:** Reviews the drafted report constructively, assigns a score out of 10, highlights strengths/areas to improve, and gives a verdict.
- **Beautiful UI:** Custom-styled Streamlit interface for seamless interaction.

## Setup & Running

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set up environment variables:
   Ensure you have a `.env` file containing your Mistral API key and your Tavily API key for web search:

   ```env
   MISTRAL_API_KEY=your_mistral_api_key
   TAVILY_API_KEY=your_tavily_api_key
   ```
   
3. Run the application:
   ```bash
   streamlit run app.py
   ```

## Architecture
- **`app.py`**: Contains the Streamlit frontend.
- **`agents.py`**: Defines the Mistral LLM configuration, custom LangChain agents (search, reader), writer and critic chains.
- **`tools.py`**: Contains the custom tools (web search, web scraping) utilized by agents.
- **`pipeline.py`** *(if applicable)*: Logic to orchestrate agents & chains together.
