import streamlit as st
import urllib.parse

st.set_page_config(page_title="SafeCheck", page_icon="🛡️", layout="centered")

# Configuration
PHONE_NUMBER = "1234567890" # Format: 447123456789
FB_USERNAME = "your.username"
DEFAULT_MSG = "I am okay, safe, and all is good in life! ❤️"

st.title("🛡️ Universal Check-In")
custom_message = st.text_area("Message Preview:", value=DEFAULT_MSG, height=120)
encoded_msg = urllib.parse.quote(custom_message)

st.divider()

col1, col2 = st.columns(2)

with col1:
    # WhatsApp
    st.link_button("🟢 WhatsApp", f"https://wa.me/{PHONE_NUMBER}?text={encoded_msg}", use_container_width=True)
    
    # Viber - Trying the direct chat protocol
    # If this doesn't open the app, your browser is blocking the 'viber://' prefix.
    st.link_button("💜 Viber", f"viber://chat?number={PHONE_NUMBER}&draft={encoded_msg}", use_container_width=True)

with col2:
    # SMS/iMessage
    st.link_button("🔵 iMessage/SMS", f"sms:{PHONE_NUMBER}&body={encoded_msg}", use_container_width=True)
    
    # Messenger
    st.link_button("🟦 Messenger", f"https://m.me/{FB_USERNAME}", use_container_width=True)

st.divider()
# Viber Fallback - Sometimes 'forward' works when 'chat' doesn't
with st.expander("Viber not opening?"):
    st.link_button("Try Viber Forward Method", f"viber://forward?text={encoded_msg}", use_container_width=True)
    st.caption("Note: If neither works, ensure Viber is installed and your browser has permission to open external apps.")
