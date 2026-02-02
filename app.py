import streamlit as st
import urllib.parse

# 1. Page Configuration
st.set_page_config(
    page_title="SafeCheck",
    page_icon="🛡️",
    layout="centered"
)

# 2. CSS to hide Header, Footer, and GitHub Icon
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            #stDecoration {display:none;}
            [data-testid="stHeader"] {display:none;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# 3. CSS for App Styling
st.markdown("""
    <style>
    div.stButton > button:first-child {
        height: 3.5em;
        font-size: 18px;
        font-weight: bold;
        border-radius: 10px;
    }
    .stTextArea textarea {
        font-size: 16px;
    }
    </style>""", unsafe_allow_html=True)

# 4. Configuration Variables
PHONE_NUMBER = "1234567890" 
FB_USERNAME = "your.username"
DEFAULT_MSG = "I am okay, safe, and all is good in life! ❤️"

# 5. App Content
st.title("🛡️ Universal Check-In")

st.subheader("Message Preview")
custom_message = st.text_area("Edit before sending:", value=DEFAULT_MSG, height=120)
encoded_msg = urllib.parse.quote(custom_message)

st.divider()
st.write("### Send via:")

col1, col2 = st.columns(2)

with col1:
    # WhatsApp
    st.link_button("🟢 WhatsApp", f"https://wa.me/{PHONE_NUMBER}?text={encoded_msg}", use_container_width=True)
    
    # Viber - Using the direct chat protocol
    st.link_button("💜 Viber", f"viber://chat?number={PHONE_NUMBER}&draft={encoded_msg}", use_container_width=True)

with col2:
    # SMS/iMessage
    st.link_button("🔵 iMessage/SMS", f"sms:{PHONE_NUMBER}&body={encoded_msg}", use_container_width=True)
    
    # Messenger
    st.link_button("🟦 Messenger", f"https://m.me/{FB_USERNAME}", use_container_width=True)

st.divider()

# Copy Button as fallback
if st.button("📋 Copy for Messenger", use_container_width=True):
    st.code(custom_message, language=None)
    st.success("Text shown above! Copy & Paste into Messenger.")

# Hidden Fallback for Viber
with st.expander("Viber not opening?"):
    st.link_button("Try Viber Forward Method", f"viber://forward?text={encoded_msg}", use_container_width=True)

st.caption(f"Contact: {PHONE_NUMBER}")
