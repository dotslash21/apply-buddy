import streamlit as st

from generators.PersonalStatementGenerator import PersonalStatementGenerator

# Initialize session state variables
if 'openai_api_key' not in st.session_state:
    st.session_state.openai_api_key = ""

# Set API keys from session state
openai_api_key = st.session_state.openai_api_key

# Streamlit app
st.set_page_config(page_title="Personal Statement Generator - ApplyBuddy", page_icon="🎓")
st.header('Personal Statement Generator')
st.markdown(
    """
    Unlock Your Potential with Our Personal Statement Generator!

    Crafting a compelling personal statement is crucial for standing out in the competitive college admissions process. 
    Our Personal Statement Generator is your go-to tool to create a captivating essay that showcases your unique 
    qualities, accomplishments, and aspirations.
    """
)

st.divider()

st.markdown(
    """
    Fill out the form below to generate a personalized personal statement that will impress admissions committees 
    and increase your chances of acceptance to your dream schools.
    """
)

# Form disabled if API key is not set
is_form_disabled = not openai_api_key or openai_api_key == ""
if is_form_disabled:
    st.warning("Please enter your OpenAI API key in the **[Settings](/Settings)** page to submit.", icon="🚨")

# Input fields
program_and_university = st.text_input("Program and university of choice", disabled=is_form_disabled)
st.caption("Examples: Master of Science in Computer Science at Stanford University, etc.")

motivation = st.text_area("Personal motivation", disabled=is_form_disabled)
st.caption("Examples: I am passionate about Computer Science because...")

personality = st.text_area("Personality traits", disabled=is_form_disabled)
st.caption("Examples: I am a hardworking and diligent individual...")

strengths_and_weaknesses = st.text_area("Strengths and weaknesses", disabled=is_form_disabled)
st.caption("Examples: My strengths include...")

interests_and_hobbies = st.text_area("Interests and hobbies", disabled=is_form_disabled)
st.caption("Examples: I enjoy playing the piano and reading...")

skills_and_experiences = st.text_area("Relevant skills and experiences", disabled=is_form_disabled)
st.caption("Examples: I have experience in...")

academic_achievements = st.text_area("Academic achievements", disabled=is_form_disabled)
st.caption("Examples: I have achieved a GPA of 4.0...")

extracurricular_activities = st.text_area("Extracurricular activities", disabled=is_form_disabled)
st.caption("Examples: I am the president of the school's chess club...")

career_goals = st.text_area("Future career goals", disabled=is_form_disabled)
st.caption("Examples: I aspire to become a software engineer...")

word_limit = st.number_input(
    "Word limit", min_value=100, max_value=1000, value=500, step=100, disabled=is_form_disabled)
st.caption("The approximate number of words you want your personal statement to be.")

# Submit button
if st.button("Generate Personal Statement", disabled=is_form_disabled):
    # Validate input
    if not program_and_university or program_and_university == "":
        st.error("Please enter your program and university of choice.", icon="🛑")
    elif not motivation:
        st.error("Please enter your personal motivation.", icon="🛑")
    elif not personality:
        st.error("Please enter your personality traits.", icon="🛑")
    elif not strengths_and_weaknesses:
        st.error("Please enter your strengths and weaknesses.", icon="🛑")
    elif not interests_and_hobbies:
        st.error("Please enter your interests and hobbies.", icon="🛑")
    elif not skills_and_experiences:
        st.error("Please enter your relevant skills and experiences.", icon="🛑")
    elif not academic_achievements:
        st.error("Please enter your academic achievements.", icon="🛑")
    elif not extracurricular_activities:
        st.error("Please enter your extracurricular activities.", icon="🛑")
    elif not career_goals:
        st.error("Please enter your future career goals.", icon="🛑")
    elif not word_limit:
        st.error("Please enter a word limit greater than 0.", icon="🛑")
    else:
        # Initialize generator
        generator = PersonalStatementGenerator(openai_api_key, model="gpt-3.5-turbo")

        # Generate personal statement
        with st.spinner("Generating..."):
            args = {
                "program_and_university": program_and_university,
                "motivation": motivation,
                "personality": personality,
                "strengths_and_weaknesses": strengths_and_weaknesses,
                "interests_and_hobbies": interests_and_hobbies,
                "skills_and_experiences": skills_and_experiences,
                "academic_achievements": academic_achievements,
                "extracurricular_activities": extracurricular_activities,
                "career_goals": career_goals,
                "word_limit": word_limit
            }
            personal_statement = generator.generate(**args)

        # Output personal statement
        st.subheader("Personal Statement")
        st.write(personal_statement)
