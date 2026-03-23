import os

os.makedirs("/opt/render/.streamlit", exist_ok=True)
with open("/opt/render/.streamlit/secrets.toml", "w") as f:
    f.write(f'SUPABASE_URL = "{os.environ["SUPABASE_URL"]}"\n')
    f.write(f'SUPABASE_KEY = "{os.environ["SUPABASE_KEY"]}"\n')
    f.write(f'GROQ_API_KEY = "{os.environ["GROQ_API_KEY"]}"\n')
