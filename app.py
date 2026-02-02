import streamlit as st
import urllib.parse
from datetime import datetime

# 1. Page Config
st.set_page_config(page_title="SafeCheck", layout="centered")

# 2. Styles (Compact)
st.markdown("<style>#MainMenu,footer,header{display:none;}"
".stApp{background-color:#0E1117;color:white;}"
".stTextArea textarea{border-radius:15px;"
"background-color:#161B22;color:white;}</style>", 
unsafe_allow_html=True)

# 3. Logic
now = datetime.now()
ts = now.strftime("%I:%M %p")
st.title("🛡️ SafeCheck")
msg = f"I am okay, safe, and all is good! ❤️\n({ts})"
txt = st.text_area("Message:", value=msg, height=140)
p_msg = urllib.parse.quote(txt)

# 4. Icon Links (Shortened to avoid line breaks)
# Using variables to keep lines tiny
IC_BASE = "https://img.icons8.com/"
W_IC = IC_BASE + "material-outlined/48/ffffff/whatsapp.png"
I_IC = IC_BASE + "ios-filled/50/ffffff/speech-bubble.png"
V_IC = IC_BASE + "ios-filled/50/ffffff/viber.png"
M_IC = IC_BASE + "material-sharp/48/ffffff/facebook-messenger.png"
O_IC = IC_BASE + "ios-glyphs/60/ffffff/external-link.png"

# 5. Grid Building (Bulletproof)
b_s = "height:75px;border-radius:18px;display:flex;"
b_s += "align-items:center;justify-content:center;"
b_s += "font-weight:600;font-size:15px;gap:10px;"
b_s += "box-shadow:0 4px 10px rgba(0,0,0,0.3);"

h = []
h.append("<div style='display:grid;grid-template-columns:1fr 1fr;gap:12px;'>")

# WhatsApp
h.append(f"<a href='whatsapp://send?text={p_msg}' target='_top'>")
h.append(f"<div style='background-color:#25D366;color:white;{b_s}'>")
h.append(f"<img src='{W_IC}' width='28'/>WhatsApp</div></a>")

# iMessage
h.append(f"<a href='sms:&body={p_msg}' target='_top'>")
h.append(f"<div style='background-color:#007AFF;color:white;{b_s}'>")
h.append(f"<img src='{I_IC}' width='24'/>iMessage</div></a>")

# Viber
h.append(f"<a
