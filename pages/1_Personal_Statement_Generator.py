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

# Input fields
personality = st.text_input("Personality traits")
motivation = st.text_input("Motivation for chosen field of study")
unique_qualities = st.text_input("Unique qualities and accomplishments")
academic_achievements = st.text_input("Academic achievements")
extracurricular_activities = st.text_input("Extracurricular activities")
career_goals = st.text_input("Career goals")

# Submit button
if not openai_api_key or openai_api_key == "":
    st.warning("Please enter your OpenAI API key in the **[Settings](/Settings)** page to submit.", icon="🚨")
elif st.button("Generate Personal Statement"):
    # Validate input
    if not personality:
        st.error("Please enter your personality traits.")
    elif not motivation:
        st.error("Please enter your motivation for chosen field of study.")
    elif not unique_qualities:
        st.error("Please enter your unique qualities and accomplishments.")
    elif not academic_achievements:
        st.error("Please enter your academic achievements.")
    elif not extracurricular_activities:
        st.error("Please enter your extracurricular activities.")
    elif not career_goals:
        st.error("Please enter your career goals.")
    else:
        # Initialize generator
        generator = PersonalStatementGenerator(openai_api_key, model="gpt-3.5-turbo")

        # Generate personal statement
        personal_statement = generator.generate(
            personality=personality,
            motivation=motivation,
            unique_qualities=unique_qualities,
            academic_achievements=academic_achievements,
            extracurricular_activities=extracurricular_activities,
            career_goals=career_goals
        )

        # Output personal statement
        st.subheader("Personal Statement")
        st.write(personal_statement)
