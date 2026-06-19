import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(
    page_title="Elite Language Translator",
    page_icon="🌍",
    layout="centered"
)

# -------------------- Session State --------------------
if "input_area" not in st.session_state:
    st.session_state.input_area = ""

if "translated_text" not in st.session_state:
    st.session_state.translated_text = ""


# -------------------- Functions --------------------
def translate_text():
    text = st.session_state.input_area.strip()

    if not text:
        st.warning("Please enter some text.")
        return

    try:
        with st.spinner("Translating..."):
            translated = GoogleTranslator(
                source=languages[st.session_state.source_lang],
                target=languages[st.session_state.target_lang]
            ).translate(text)

        st.session_state.translated_text = translated

    except Exception as e:
        st.error(f"Translation failed:\n{e}")


def clear_input():
    st.session_state.input_area = ""


def clear_all():
    st.session_state.input_area = ""
    st.session_state.translated_text = ""


# -------------------- Languages --------------------
languages = {
    "Spanish": "es",
    "English": "en",
    "Telugu": "te",
    "Hindi": "hi",
    "Tamil": "ta",
    "Kannada": "kn",
    "Malayalam": "ml",
    "Marathi": "mr",
    "Gujarati": "gu",
    "Punjabi": "pa",
    "Bengali": "bn",
    "Urdu": "ur",
    "Odia": "or",
    "Assamese": "as",
    "Sanskrit": "sa",
    "French": "fr",
    "German": "de",
    "Italian": "it",
    "Portuguese": "pt",
    "Russian": "ru",
    "Japanese": "ja",
    "Korean": "ko",
    "Chinese (Simplified)": "zh-CN",
    "Chinese (Traditional)": "zh-TW",
    "Arabic": "ar",
    "Turkish": "tr",
    "Dutch": "nl",
    "Polish": "pl",
    "Thai": "th",
    "Vietnamese": "vi",
    "Indonesian": "id",
    "Malay": "ms",
    "Filipino": "tl",
    "Greek": "el",
    "Hebrew": "iw",
    "Persian": "fa",
    "Ukrainian": "uk",
    "Romanian": "ro",
    "Hungarian": "hu",
    "Czech": "cs",
    "Slovak": "sk",
    "Bulgarian": "bg",
    "Croatian": "hr",
    "Serbian": "sr",
    "Slovenian": "sl",
    "Danish": "da",
    "Swedish": "sv",
    "Norwegian": "no",
    "Finnish": "fi",
    "Lithuanian": "lt",
    "Latvian": "lv",
    "Estonian": "et",
    "Swahili": "sw",
    "Afrikaans": "af",
    "Albanian": "sq",
    "Belarusian": "be",
    "Catalan": "ca",
    "Irish": "ga",
    "Maltese": "mt",
    "Welsh": "cy"
}

# -------------------- UI --------------------
st.title("🌍 Elite Language Translator")
st.markdown("### Translate between 60+ languages instantly")

col1, col2 = st.columns(2)

with col1:
    st.selectbox(
        "Source Language",
        options=list(languages.keys()),
        index=list(languages.keys()).index("English"),
        key="source_lang"
    )

with col2:
    st.selectbox(
        "Target Language",
        options=list(languages.keys()),
        index=list(languages.keys()).index("Spanish"),
        key="target_lang"
    )

st.text_area(
    "Enter Text",
    height=220,
    placeholder="Type or paste your text here...",
    key="input_area"
)

col1, col2 = st.columns(2)

with col1:
    st.button(
        "🔥 Translate",
        use_container_width=True,
        type="primary",
        on_click=translate_text
    )

with col2:
    st.button(
        "🗑 Clear Input",
        use_container_width=True,
        on_click=clear_input
    )

# -------------------- Output --------------------
if st.session_state.translated_text:

    st.success("✅ Translation Completed")

    st.markdown("### Translated Text")

    # Automatically includes a Copy button
    st.code(
        st.session_state.translated_text,
        language=None
    )

    st.button(
        "🗑 Clear All",
        use_container_width=True,
        on_click=clear_all
    )

st.divider()
st.caption("🌍 Powered by Google Translate | Built with Streamlit ❤️")
