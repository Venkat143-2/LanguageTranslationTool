import streamlit as st

st.set_page_config(
    page_title="Language Translator",
    page_icon="🌍",
    layout="centered",
    initial_sidebar_state="collapsed",  # Hides ugly sidebar
)

# Hide default Streamlit branding (looks pro)
hide_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_style, unsafe_allow_html=True)

st.title("🌍 Language Translator")
st.markdown("#### Translate text between 60+ languages, instantly and for free.")

col1, col2, col3 = st.columns(3)
with col1: st.metric("Languages", "60+")
with col2: st.metric("Speed", "Instant")
with col3: st.metric("Cost", "Free")

with st.container(border=True):
    st.markdown("**What you can do here**")
    st.markdown("""
        - Translate between 60+ languages  
        - Swap source and target languages in one click  
        - Copy your translation straight to the clipboard
    """)

_, mid, _ = st.columns([1, 2, 1])
with mid:
    if st.button("🚀 Start Translating", use_container_width=True, type="primary"):
        st.switch_page("pages/Translator.py")   # Fixed path

with st.expander("🌐 Preview supported languages"):
    preview = [
        "Spanish", "English", "Hindi", "Telugu", "Tamil", "Kannada", "Malayalam",
        "Marathi", "Gujarati", "Punjabi", "Bengali", "Urdu", "French", "German",
        "Italian", "Portuguese", "Russian", "Japanese", "Korean", "Chinese",
        "Arabic", "Turkish", "Dutch", "and 35+ more...",
    ]
    st.write(", ".join(preview))

st.divider()
st.caption("© 2026 Language Translator • Fast • Accurate • Secure")
