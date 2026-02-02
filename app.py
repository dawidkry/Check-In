import streamlit as st
import urllib.parse

# 1. Page Configuration
st.set_page_config(page_title="SafeCheck", page_icon="🛡️", layout="centered")

# 2. THE STYLING ENGINE
# We target both Streamlit buttons and our custom HTML button to match exactly
brand_color = "#1A73E8"  # Professional Blue

st.markdown(f"""
    <style>
    /* Hide Streamlit junk */
    #MainMenu, footer, header, [data-testid="stHeader"] {{visibility: hidden; display:none;}}
    
    /* Style the Text Area */
    .stTextArea textarea {{
        border-radius: 15px;
        border: 2px solid {brand_color};
    }}

    /* Style Streamlit Buttons */
    div.stButton > button {{
        background-color: {brand_color} !important;
        color: white !important;
        height: 4em !important;
        width: 100% !important;
        border-radius: 12px !important;
        border: none !important;
        font-size: 18px !important;
        font-weight: 600 !important;
        transition: 0.3s;
    }}
    
    /* Style Link Buttons (WhatsApp/Viber/SMS) */
    div.stLinkButton > a {{
        background-color: {brand_color} !important;
        color: white !important;
        height: 4em !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        border-radius: 12px !important;
        text-decoration: none !important;
        font-size: 18px !important;
        font-weight: 600 !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# 3. App Content
st.title("🛡️ SafeCheck")

DEFAULT_MSG = "I am okay, safe, and all is good in life! ❤️"
custom_message = st.text_area("Edit Message:", value=DEFAULT_MSG, height=120)
encoded_msg = urllib.parse.quote(custom_message)

st.write("### Choose your app:")

# 4. The Grid
col1, col2 = st.columns(2)

with col1:
    st.link_button("WhatsApp", f"whatsapp://send?text={encoded_msg}", use_container_width=True)
    st.link_button("Viber", f"viber://forward?text={encoded_msg}", use_container_width=True)

with col2:
    st.link_button("SMS / iMessage", f"sms:&body={encoded_msg}", use_container_width=True)
    
    # 5. The Messenger/Share Sheet Button (Styling injected inside the component)
    share_js = f"""
    <style>
        button {{
            width: 100%;
            height: 4em;
            background-color: {brand_color};
            color: white;
            border: none;
            border-radius: 12px;
            font-size: 18px;
            font-weight: 600;
            cursor: pointer;
            font-family: sans-serif;
        }}
    </style>
    <button onclick="share()">Messenger / All</button>
    <script>
    function share() {{
        if (navigator.share) {{
            navigator.share({{ text: `{custom_message}` }});
        }} else {{
            alert('Share not supported');
        }}
    }}
    </script>
    """
    st.components.v1.html(share_js, height=85)

st.divider()
st.caption("Customizable Safety Launcher • One-tap protection")
