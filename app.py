import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(
    page_title="AI Language Translator",
    page_icon="🌍"
)

st.title("🌍 AI Language Translation Tool")
st.markdown("### Welcome! 👋")
st.write("This AI-powered application translates text instantly between multiple languages using Google Translator.")

languages = [
    "english", "tamil", "hindi", "telugu", "kannada",
    "malayalam", "french", "german", "spanish",
    "italian", "japanese", "korean", "chinese", "arabic"
]

if "text" not in st.session_state:
    st.session_state.text = ""

text = st.text_area(
    "Enter the text to translate:",
    key="text"
)

if st.button("🗑️ Clear"):
    st.session_state.text = ""
    st.rerun()

source = st.selectbox("Source Language", languages)
target = st.selectbox("Target Language", languages)

if st.button("Translate"):
    if text.strip():
        try:
            translated = GoogleTranslator(
                source=source,
                target=target
            ).translate(text)

            st.success("Translation Completed Successfully ✅")
            st.subheader("Translated Text")
            st.write(translated)

        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter some text.")