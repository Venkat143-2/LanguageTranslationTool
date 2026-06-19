import streamlit as st

st.set_page_config(
    page_title="Language Translator",
    page_icon="🌍",
    layout="centered",
)

st.title("🌍 Language Translator")
st.markdown("#### Translate text between 60+ languages, instantly and for free.")

st.write("")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Languages", "60+")
with col2:
    st.metric("Speed", "Instant")
with col3:
    st.metric("Cost", "Free")

st.write("")

with st.container(border=True):
    st.markdown("**What you can do here**")
    st.markdown(
        "- Translate between 60+ languages\n"
        "- Swap source and target languages in one click\n"
        "- Copy your translation straight to the clipboard"
    )

st.write("")

_, mid, _ = st.columns([1, 2, 1])
with mid:
    if st.button("🚀 Start Translating", use_container_width=True, type="primary"):
        st.switch_page("pages/Language Translator.py")

st.write("")
with st.expander("🌐 Preview supported languages"):
    preview = [
        "Spanish", "English", "Hindi", "Telugu", "Tamil", "Kannada", "Malayalam",
        "Marathi", "Gujarati", "Punjabi", "Bengali", "Urdu", "French", "German",
        "Italian", "Portuguese", "Russian", "Japanese", "Korean", "Chinese",
        "Arabic", "Turkish", "Dutch", "and 35+ more...",
    ]
    st.write(", ".join(preview))

st.divider()
st.caption("© 2026 Elite Language Translator • Fast • Accurate • Secure")
