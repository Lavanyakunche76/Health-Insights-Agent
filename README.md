# HIA (Health Insights Agent)

AI Agent to analyze blood reports and provide detailed health insights.

## Features

- **Analysis Agent**: Report analysis with in-context learning
- **Chat Agent**: RAG-powered follow-up Q&A (FAISS + HuggingFace)
- **Multi-model cascade** via Groq with automatic fallback
- **Chat sessions**: Multiple analysis sessions stored in Supabase
- **PDF handling**: Upload up to 20MB, max 50 pages
- **Secure auth**: Supabase Auth sign up and sign in
- **Modern UI**: Responsive Streamlit app

## Tech Stack

- **Frontend**: Streamlit
- **AI/LLM**: Groq with multi-model fallback
- **Embeddings**: HuggingFace all-MiniLM-L6-v2, FAISS
- **Database**: Supabase PostgreSQL
- **Libraries**: LangChain, sentence-transformers, PDFPlumber

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Lavanyakunche76/Health-Insights-Agent.git
cd Health-Insights-Agent
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create `.streamlit/secrets.toml`:

```toml
SUPABASE_URL = "your-supabase-url"
SUPABASE_KEY = "your-supabase-key"
GROQ_API_KEY = "your-groq-api-key"
```

4. Set up Supabase database using `public/db/script.sql`

5. Run the application:

```bash
streamlit run src/main.py
```

## License

This project is licensed under the MIT License.

## Author

Created by [Lavanya Kunche](https://github.com/Lavanyakunche76)
