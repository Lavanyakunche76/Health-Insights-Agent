# ðŸ©º HIA (Health Insights Agent)

AI Agent to analyze blood reports and provide detailed health insights.

<p align="center">
  <a href="https://github.com/Lavanyakunche76/hia/issues"><img src="https://img.shields.io/github/issues/Lavanyakunche76/hia"></a> 
  <a href="https://github.com/Lavanyakunche76/hia/stargazers"><img src="https://img.shields.io/github/stars/Lavanyakunche76/hia"></a>
  <a href="https://github.com/Lavanyakunche76/hia/network/members"><img src="https://img.shields.io/github/forks/Lavanyakunche76/hia"></a>
  <a href="https://github.com/Lavanyakunche76/hia/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-blue.svg">
  </a>
</p>

<p align="center">
  <a href="#-features">Features</a> |
  <a href="#%EF%B8%8F-tech-stack">Tech Stack</a> |
  <a href="#-installation">Installation</a> |
  <a href="#-project-structure">Project Structure</a> |
  <a href="#-contributing">Contributing</a> |
  <a href="#%EF%B8%8F-author">Author</a>
</p>

<p align="center">
  <a href="https://github.com/Lavanyakunche76/hia"><img src="https://raw.githubusercontent.com/Lavanyakunche76/hia/main/public/HIA_demo.gif" alt="Usage Demo"></a>
</p>

## ðŸŒŸ Features

- **Agent-based architecture**
  - **Analysis Agent**: Report analysis with in-context learning from previous analyses and a built-in knowledge base
  - **Chat Agent**: RAG-powered follow-up Q&A over your report (FAISS + HuggingFace embeddings)
- **Multi-model cascade** via Groq with automatic fallback (primary â†’ secondary â†’ tertiary â†’ fallback)
- **Chat sessions**: Create multiple analysis sessions; each session stores report, analysis, and follow-up messages in Supabase
- **Report sources**: Upload your own PDF or use the built-in sample report for quick testing
- **PDF handling**: Upload up to 20MB, max 50 pages; validation for file type and medical-report content
- **Daily analysis limit**: Configurable cap (default 15/day) with countdown in the sidebar
- **Secure auth**: Supabase Auth (sign up / sign in), session validation, and configurable session timeout
- **Session history**: View, switch, and delete past sessions; report text persisted for follow-up chat across reloads
- **Modern UI**: Responsive Streamlit app with sidebar session list, user greeting, and real-time feedback

## ðŸ› ï¸ Tech Stack

- **Frontend**: Streamlit (1.42+)
- **AI / LLM**
  - **Report analysis**: Groq with multi-model fallback via `ModelManager`
    - Primary: `meta-llama/llama-4-maverick-17b-128e-instruct`
    - Secondary: `llama-3.3-70b-versatile`
    - Tertiary: `llama-3.1-8b-instant`
    - Fallback: `llama3-70b-8192`
  - **Follow-up chat**: RAG with LangChain, HuggingFace embeddings (`all-MiniLM-L6-v2`), FAISS vector store, and Groq (`llama-3.3-70b-versatile`)
- **Database**: Supabase (PostgreSQL)
  - Tables: `users`, `chat_sessions`, `chat_messages`
- **Auth**: Supabase Auth, Gotrue
- **PDF**: PDFPlumber (text extraction), filetype (file validation)
- **Libraries**: LangChain, LangChain Community, LangChain HuggingFace, LangChain Text Splitters, sentence-transformers, FAISS (CPU)

## ðŸš€ Installation

#### Requirements ðŸ“‹

- Python 3.8+
- Streamlit 1.42+
- Supabase account
- Groq API key
- PDFPlumber, filetype

#### Getting Started ðŸ“

1. Clone the repository:

```bash
git clone https://github.com/Lavanyakunche76/hia.git
cd hia
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Required environment variables (in `.streamlit/secrets.toml`):

```toml
SUPABASE_URL = "your-supabase-url"
SUPABASE_KEY = "your-supabase-key"
GROQ_API_KEY = "your-groq-api-key"
```

4. Set up Supabase database schema:

The application uses three tables: `users`, `chat_sessions`, and `chat_messages`. Use the SQL script at `public/db/script.sql` to create them.

![database schema](https://raw.githubusercontent.com/Lavanyakunche76/hia/main/public/db/schema.png)

(You can turn off email confirmation on signup in Supabase: **Authentication â†’ Providers â†’ Email â†’ Confirm email**.)

5. Run the application:

```bash
streamlit run src\main.py
```

## ðŸ“ Project Structure

```
hia/
â”œâ”€â”€ requirements.txt
â”œâ”€â”€ README.md
â”œâ”€â”€ src/
â”‚   â”œâ”€â”€ main.py                 # Application entry point; chat UI and session flow
â”‚   â”œâ”€â”€ auth/
â”‚   â”‚   â”œâ”€â”€ auth_service.py     # Supabase auth, sessions, chat message persistence
â”‚   â”‚   â””â”€â”€ session_manager.py # Session init, timeout, create/delete chat sessions
â”‚   â”œâ”€â”€ components/
â”‚   â”‚   â”œâ”€â”€ analysis_form.py    # Report source (upload/sample), patient form, analysis trigger
â”‚   â”‚   â”œâ”€â”€ auth_pages.py       # Login / signup pages
â”‚   â”‚   â”œâ”€â”€ footer.py           # Footer component
â”‚   â”‚   â”œâ”€â”€ header.py           # User greeting
â”‚   â”‚   â””â”€â”€ sidebar.py          # Session list, new session, daily limit, logout
â”‚   â”œâ”€â”€ config/
â”‚   â”‚   â”œâ”€â”€ app_config.py       # App name, limits (upload, pages, analysis, timeout)
â”‚   â”‚   â”œâ”€â”€ prompts.py          # Specialist prompts for report analysis
â”‚   â”‚   â””â”€â”€ sample_data.py      # Sample blood report for "Use Sample PDF"
â”‚   â”œâ”€â”€ services/
â”‚   â”‚   â””â”€â”€ ai_service.py       # Analysis + chat entry points; vector store caching
â”‚   â”œâ”€â”€ agents/
â”‚   â”‚   â”œâ”€â”€ analysis_agent.py   # Report analysis, rate limits, knowledge base, in-context learning
â”‚   â”‚   â”œâ”€â”€ chat_agent.py       # RAG pipeline (embeddings, FAISS, query contextualization)
â”‚   â”‚   â””â”€â”€ model_manager.py   # Groq multi-model cascade and fallback
â”‚   â””â”€â”€ utils/
â”‚       â”œâ”€â”€ validators.py       # Email, password, PDF file and content validation
â”‚       â””â”€â”€ pdf_extractor.py   # PDF text extraction and validation
â”œâ”€â”€ public/
â”‚   â””â”€â”€ db/
â”‚       â”œâ”€â”€ script.sql          # Supabase schema (users, chat_sessions, chat_messages)
â”‚       â””â”€â”€ schema.png          # Schema diagram
```

## ðŸ‘¥ Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) for details on how to submit pull requests, the development workflow, coding standards, and more.

We appreciate all contributions, from reporting bugs and improving documentation to implementing new features.

## ðŸ‘¨â€ðŸ’» Contributors

Thanks to all the amazing contributors who have helped improve this project!

| Avatar | Name | GitHub | Role | Contributions | PR(s) | Notes |
|--------|------|--------|------|---------------|-------|-------|
| <img src="https://github.com/harshhh28.png" width="50px" height="50px" alt="harshhh28 avatar"/> | Lavanya Kunche | [Lavanyakunche76](https://github.com/Lavanyakunche76) | Project Creator & Maintainer | Core implementation, Documentation | N/A | Lead Developer |
| <img src="https://github.com/gaurav98095.png" width="50px" height="50px" alt="gaurav98095 avatar"/> | Gaurav | [gaurav98095](https://github.com/gaurav98095) | Contributor | DB Schema, bugs | [#1](https://github.com/Lavanyakunche76/hia/pull/1), [#5](https://github.com/Lavanyakunche76/hia/pull/5), [#6](https://github.com/Lavanyakunche76/hia/pull/6), [#7](https://github.com/Lavanyakunche76/hia/pull/7) | Database Design, bugs |

<!-- To future contributors: Your profile will be added here when your PR is merged! -->

## ðŸ“„ License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/Lavanyakunche76/hia/blob/main/LICENSE) file for details.

## ðŸ™‹â€â™‚ï¸ Author

Created by [Lavanya Kunche](https://github.com/Lavanyakunche76)
