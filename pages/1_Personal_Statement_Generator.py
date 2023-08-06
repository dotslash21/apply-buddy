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
program_and_university = st.text_input("Program and university of choice")
st.caption("Examples: Master of Science in Computer Science at Stanford University, etc.")

motivation = st.text_area("Personal motivation")
st.caption("Examples: I am passionate about Computer Science because...")

personality = st.text_area("Personality traits")
st.caption("Examples: I am a hardworking and diligent individual...")

strengths_and_weaknesses = st.text_area("Strengths and weaknesses")
st.caption("Examples: My strengths include...")

interests_and_hobbies = st.text_area("Interests and hobbies")
st.caption("Examples: I enjoy playing the piano and reading...")

skills_and_experiences = st.text_area("Relevant skills and experiences")
st.caption("Examples: I have experience in...")

academic_achievements = st.text_area("Academic achievements")
st.caption("Examples: I have achieved a GPA of 4.0...")

extracurricular_activities = st.text_area("Extracurricular activities")
st.caption("Examples: I am the president of the school's chess club...")

career_goals = st.text_area("Future career goals")
st.caption("Examples: I aspire to become a software engineer...")

word_limit = st.number_input("Word limit", min_value=100, max_value=1000, value=500, step=100)
st.caption("The approximate number of words you want your personal statement to be.")

# Submit button
if not openai_api_key or openai_api_key == "":
    st.warning("Please enter your OpenAI API key in the **[Settings](/Settings)** page to submit.", icon="🚨")
elif st.button("Generate Personal Statement"):
    # Validate input
    if not program_and_university or program_and_university == "":
        st.warning("Please enter your program and university of choice.")
    elif not motivation:
        st.error("Please enter your personal motivation.")
    elif not personality:
        st.error("Please enter your personality traits.")
    elif not strengths_and_weaknesses:
        st.error("Please enter your strengths and weaknesses.")
    elif not interests_and_hobbies:
        st.error("Please enter your interests and hobbies.")
    elif not skills_and_experiences:
        st.error("Please enter your relevant skills and experiences.")
    elif not academic_achievements:
        st.error("Please enter your academic achievements.")
    elif not extracurricular_activities:
        st.error("Please enter your extracurricular activities.")
    elif not career_goals:
        st.error("Please enter your future career goals.")
    elif not word_limit:
        st.error("Please enter a word limit greater than 0.")
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
