import streamlit as st

# Initialize session state variables
if 'openai_api_key' not in st.session_state:
    st.session_state.openai_api_key = ""

st.set_page_config(page_title="Home - ApplyBuddy", page_icon="🎓")

st.header("Introducing ApplyBuddy 🎓")
st.subheader("Your college application companion!")

st.divider()

st.markdown(
    """
    ApplyBuddy is a comprehensive and easy-to-use application that harnesses the cutting-edge capabilities of 
    large language models like OpenAI's ChatGPT to help you streamline and elevate your college application process. 
    With a wide range of professional services, we aim to empower aspiring students like you to craft compelling and 
    persuasive application documents that will leave a lasting impression on admissions committees.
    
    #### 💼 Services:
    
    **Personal Statement** - Craft a powerful personal statement with the aid of large language models. We help 
    you articulate your personality, motivation, and unique qualities, ensuring your application stands out.
    
    **Statement of Purpose** - Create a captivating statement of purpose that showcases your unique qualities,
    accomplishments, and aspirations. We help you craft a compelling narrative that will impress admissions committees.
    
    ApplyBuddy is committed to helping you achieve your college goals. With our AI-powered assistance, you can craft 
    application documents that will impress admissions committees and increase your chances of acceptance to your 
    dream schools.
    
    Let ApplyBuddy, powered by advanced language models, be your trusted ally on the path to college success!
    """
)
