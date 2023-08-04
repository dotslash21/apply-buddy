import streamlit as st

# Initialize session state variables
if 'openai_api_key' not in st.session_state:
    st.session_state.openai_api_key = ""

# Streamlit app
st.set_page_config(page_title="Settings - ApplyBuddy", page_icon="🎓")
st.subheader('Settings')

# Get API keys
openai_api_key = st.text_input("OpenAI API Key", value=st.session_state.openai_api_key, type="password")
st.caption("*Required for all services; get it [here](https://platform.openai.com/account/api-keys).*")

# If the 'Save' button is clicked
if st.button("Save"):
    if not openai_api_key.strip():
        st.error("Please provide the missing API key.")
    else:
        st.session_state.openai_api_key = openai_api_key
        st.success("Settings saved successfully!")
