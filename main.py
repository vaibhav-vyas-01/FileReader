import streamlit as st

# વેબ પેજનું ટાઈટલ અને સેટિંગ્સ
st.set_page_config(page_title="FileReader 1.1", page_icon="🔊")

st.title("Welcome to FileReader 1.1")
st.caption("Created by Vaibhav")

# input tabs from user.
tab1, tab2 = st.tabs(["📄 Upload File", "✍️ Enter Text"])

text_to_speak = ""

with tab1:
    uploaded_file = st.file_uploader("Choose a text file", type=["txt"])
    if uploaded_file is not None:
        # ફાઈલ રીડ કરીને સિંગલ લાઈનમાં કન્વર્ટ કરવી
        bytes_data = uploaded_file.read()
        text_to_speak = bytes_data.decode("utf-8").replace("\n", " ")
        st.text_area("File Content:", text_to_speak, height=150)

with tab2:
    user_text = st.text_area("Enter your text here:")
    if user_text:
        text_to_speak = user_text.replace("\n", " ")

# બ્રાઉઝરના સ્પીચ એન્જિન (JavaScript) નો ઉપયોગ કરીને અવાજ પ્લે કરવો
if text_to_speak:
    if st.button("🔊 Speak Now"):
        # JavaScript કોડ જે બ્રાઉઝરના સ્પીકરનો ઉપયોગ કરશે
        js_code = f"""
        <script>
            var msg = new SpeechSynthesisUtterance('{text_to_speak.replace("'", "\\'")}');
            window.speechSynthesis.speak(msg);
        </script>
        """
        # આ કોડને વેબ પેજમાં છૂપો રન કરવો જેથી અવાજ આવે
        st.components.v1.html(js_code, height=0)
