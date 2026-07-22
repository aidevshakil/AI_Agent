PAGE_CONFIG = {
    "page_title": "AI Agent Chatbot",
    "page_icon": "🤖",
    "layout": "wide",
    "initial_sidebar_state": "expanded"
}

GROQ_CONFIG = {
    "temperature": 0.7,
    "max_tokens": 1000,
    "message_history_limit": 10
}

AVAILABLE_MODELS = [
    "llama-3.3-70b-versatile",
    "llama-3.1-70b-versatile",
    "gemma-2-9b-it",
    "mixtral-8x7b-32768"
]

DEFAULT_MODEL = "llama-3.3-70b-versatile"

UI_CONFIG = {
    "chat_height": 400,
    "sidebar_width": "expanded"
}

CSS = """
<style>
    .main { padding-top: 2rem; }
    .personality-badge {
        background-color: #1f77b4;
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 0.5rem;
        font-weight: bold;
    }
    .model-info {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
</style>
"""

ERROR_MESSAGES = {
    "api_key_not_configured": "❌ Error: GROQ_API_KEY not configured. Please set your API key in Streamlit secrets.",
    "api_error": "❌ Error: {error}",
    "invalid_personality": "❌ Error: Invalid personality selected."
}

SUCCESS_MESSAGES = {
    "api_connected": "✅ Groq API Connected",
    "api_disconnected": "❌ Groq API Not Connected"
}

INFO_MESSAGES = {
    "set_api_key": "Please set GROQ_API_KEY in your .streamlit/secrets.toml file",
    "about_section": """
    This AI Agent Chatbot uses **Groq API** to generate intelligent responses.

    Each personality has specific constraints:
    - **Math Teacher**: Math questions only
    - **Doctor**: Health & medical questions only
    - **Travel Guide**: Travel & tourism questions only
    - **Chef**: Cooking & recipe questions only
    - **Tech Support**: Technical support questions only
    """
}

SESSION_STATE_DEFAULTS = {
    "messages": [],
    "selected_personality": "Math Teacher",
    "selected_model": DEFAULT_MODEL,
}
