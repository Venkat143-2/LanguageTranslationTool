import json

import streamlit as st
import streamlit.components.v1 as components
from deep_translator import GoogleTranslator

st.set_page_config(
    page_title="Translator | Elite Language Translator",
    page_icon="🌍",
    layout="centered",
)

LANGUAGES = {
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
    "Welsh": "cy",
}
LANGUAGE_NAMES = list(LANGUAGES.keys())

# --- session state defaults ---
if "input_area" not in st.session_state:
    st.session_state.input_area = ""
if "translated_text" not in st.session_state:
    st.session_state.translated_text = ""
if "source_lang" not in st.session_state:
    st.session_state.source_lang = "Spanish"   # default source
if "target_lang" not in st.session_state:
    st.session_state.target_lang = "English"   # default target


def translate_text():
    text = st.session_state.input_area.strip()
    if not text:
        st.warning("Please enter some text.")
        return
    try:
        with st.spinner("Translating..."):
            translated = GoogleTranslator(
                source=LANGUAGES[st.session_state.source_lang],
                target=LANGUAGES[st.session_state.target_lang],
            ).translate(text)
        st.session_state.translated_text = translated
    except Exception as e:
        st.error(f"Translation failed:\n{e}")


def clear_input():
    st.session_state.input_area = ""


def clear_all():
    st.session_state.input_area = ""
    st.session_state.translated_text = ""


def swap_languages():
    st.session_state.source_lang, st.session_state.target_lang = (
        st.session_state.target_lang,
        st.session_state.source_lang,
    )


def copy_to_clipboard_button(text: str, label: str = "📋 Copy"):
    """
    Copies `text` to the clipboard inside the user's BROWSER via JavaScript.
    pyperclip needed a clipboard tool (xclip/xsel) on the SERVER, which the
    Streamlit Cloud sandbox doesn't have - that was the cause of the crash.
    Clipboard access has to happen client-side, so this renders a tiny HTML
    button that calls the browser's Clipboard API instead.
    """
    safe_text = json.dumps(text)
    components.html(
        f"""
        <button id="copy-btn" style="
            width:100%; padding:0.55em 1em; border-radius:0.5em;
            border:1px solid rgba(49,51,63,0.2); background-color:#ffffff;
            cursor:pointer; font-size:0.95rem;
        ">{label}</button>
        <script>
        const btn = document.getElementById("copy-btn");
        btn.addEventListener("click", async () => {{
            const text = {safe_text};
            try {{
                await navigator.clipboard.writeText(text);
            }} catch (err) {{
                const ta = document.createElement("textarea");
                ta.value = text;
                document.body.appendChild(ta);
                ta.select();
                document.execCommand("copy");
                document.body.removeChild(ta);
            }}
            btn.innerText = "✅ Copied!";
            setTimeout(() => {{ btn.innerText = "{label}"; }}, 1500);
        }});
        </script>
        """,
        height=48,
    )


st.page_link("Home.py", label="Back to Home", icon="🏠")

st.title("🌍 Translator")
st.caption("Translate between 60+ languages instantly")

col1, col2 = st.columns(2)
with col1:
    st.selectbox("Source Language", options=LANGUAGE_NAMES, key="source_lang")
with col2:
    st.selectbox("Target Language", options=LANGUAGE_NAMES, key="target_lang")

_, mid, _ = st.columns([2, 1, 2])
with mid:
    st.button("🔄 Swap", use_container_width=True, on_click=swap_languages)

st.text_area(
    "Enter Text",
    height=220,
    placeholder="Type or paste your text here...",
    key="input_area",
)

col1, col2 = st.columns(2)
with col1:
    st.button(
        "🔥 Translate",
        use_container_width=True,
        type="primary",
        on_click=translate_text,
    )
with col2:
    st.button("🗑 Clear Input", use_container_width=True, on_click=clear_input)

if st.session_state.translated_text:
    st.success("Translated Text")
    st.text_area(
        "Result",
        value=st.session_state.translated_text,
        height=220,
        disabled=True,
    )
    col1, col2 = st.columns(2)
    with col1:
        copy_to_clipboard_button(st.session_state.translated_text)
    with col2:
        st.button("🗑 Clear All", use_container_width=True, on_click=clear_all)

st.divider()
st.caption("🌍 Powered by Google Translate | Built with Streamlit")
