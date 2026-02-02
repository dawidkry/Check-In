import streamlit as st
import urllib.parse

# Page Config for mobile browser optimization
st.set_page_config(
    page_title="SafeCheck", 
    page_icon="✅", 
    layout="centered"
)

# Custom CSS to make buttons look like mobile app buttons
st.markdown("""
    <style>
    div.stButton > button:first-child {
        height: 3em;
        font-size: 20px;
        font-weight: bold;
    }
    </style>""", unsafe_allow_html=True)

st.title("🛡️ Safety Check-In")

# Settings - You can change these anytime in GitHub
PHONE_NUMBER = "1234567890" # Example: 15551234567
MESSAGE_TEMPLATE = "I am okay, safe, and all is good in life! ❤️"

# Message Customization Area
st.subheader("Current Message:")
final_message = st.text_area("Edit if needed:", value=MESSAGE_TEMPLATE, height=150)

# URL Encoding
encoded_text = urllib.parse.quote(final_message)

# Selection Columns
col1, col2 = st.columns(2)

with col1:
    wa_link = f"https://wa.me/{PHONE_NUMBER}?text={encoded_text}"
    st.link_button("🟢 WhatsApp", wa_link, use_container_width=True)

with col2:
    # 'sms:' works for both iOS and Android
    sms_link = f"sms:{PHONE_NUMBER}&body={encoded_text}"
    st.link_button("🔵 iMessage/SMS", sms_link, use_container_width=True)

st.divider()
st.caption(f"Recipient set to: {PHONE_NUMBER}")
