import streamlit as st
from openai import OpenAI
import os
from typing import Optional, List, Dict, Tuple

from config import (
    PAGE_CONFIG, GROQ_CONFIG, AVAILABLE_MODELS, CSS, ERROR_MESSAGES,
    SUCCESS_MESSAGES, INFO_MESSAGES, SESSION_STATE_DEFAULTS
)
from personalities import (
    get_all_personalities, get_personality_description, get_system_prompt
)


@st.cache_resource
def get_groq_client() -> Optional[OpenAI]:
    api_key = st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")
    if not api_key:
        return None
    return OpenAI(
        api_key=api_key,
        base_url="https://api.groq.com/openai/v1"
    )


def init_session_state() -> None:
    for key, value in SESSION_STATE_DEFAULTS.items():
        if key not in st.session_state:
            st.session_state[key] = value


def build_messages(user_message: str, personality: str) -> List[Dict[str, str]]:
    return [
        {"role": "system", "content": get_system_prompt(personality)},
        *st.session_state.messages[-GROQ_CONFIG["message_history_limit"]:],
        {"role": "user", "content": user_message}
    ]


def get_ai_response(user_message: str, personality: str, model: str) -> str:
    client = st.session_state.get("groq_client")
    if not client:
        return ERROR_MESSAGES["api_key_not_configured"]

    try:
        messages = build_messages(user_message, personality)
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=GROQ_CONFIG["temperature"],
            max_tokens=GROQ_CONFIG["max_tokens"],
        )
        return response.choices[0].message.content
    except Exception as e:
        return ERROR_MESSAGES["api_error"].format(error=str(e))


def render_sidebar() -> Tuple[str, str]:
    with st.sidebar:
        st.header("⚙️ Configuration")

        st.subheader("Select Personality")
        personality = st.radio(
            "Choose your chatbot personality:",
            get_all_personalities(),
            key="personality_radio"
        )
        st.markdown(f"**Description:** {get_personality_description(personality)}")
        st.markdown("---")

        st.subheader("Select AI Model")
        model = st.selectbox(
            "Choose your AI model:",
            AVAILABLE_MODELS,
            key="model_select"
        )
        st.markdown("---")

        st.subheader("API Status")
        if st.session_state.get("groq_client"):
            st.success(SUCCESS_MESSAGES["api_connected"])
        else:
            st.error(SUCCESS_MESSAGES["api_disconnected"])
            st.info(INFO_MESSAGES["set_api_key"])

        st.markdown("---")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("➕ New Chat", use_container_width=True):
                st.session_state.messages = []
                st.rerun()
        with col2:
            if st.button("🗑️ Clear All", use_container_width=True):
                st.session_state.messages = []
                st.rerun()

        st.markdown("---")
        st.subheader("ℹ️ About")
        st.markdown(INFO_MESSAGES["about_section"])

    return personality, model


def render_chat_header(personality: str, model: str) -> None:
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown(f"### Current Personality: **{personality}**")
    with col2:
        st.markdown(f"**Model:** `{model}`")
    st.markdown("---")


def render_chat_messages() -> None:
    chat_container = st.container(height=400)
    with chat_container:
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])


def handle_user_input(user_input: str, personality: str, model: str) -> None:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = get_ai_response(user_input, personality, model)
            st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})
    st.rerun()


def main():
    st.set_page_config(**PAGE_CONFIG)
    st.markdown(CSS, unsafe_allow_html=True)
    st.title("🤖 AI Agent Chatbot")
    st.markdown("---")

    init_session_state()

    if "groq_client" not in st.session_state:
        st.session_state.groq_client = get_groq_client()

    personality, model = render_sidebar()
    st.session_state.selected_personality = personality
    st.session_state.selected_model = model

    render_chat_header(personality, model)
    render_chat_messages()

    st.markdown("---")
    user_input = st.chat_input(
        f"Ask {personality} a question...",
        key="chat_input"
    )

    if user_input:
        handle_user_input(user_input, personality, model)


if __name__ == "__main__":
    main()
