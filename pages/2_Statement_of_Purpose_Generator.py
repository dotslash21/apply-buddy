import streamlit as st

from generators.StatementOfPurposeGenerator import StatementOfPurposeGenerator

# Initialize session state variables
if 'openai_api_key' not in st.session_state:
    st.session_state.openai_api_key = ""

# Set API keys from session state
openai_api_key = st.session_state.openai_api_key

# Streamlit app
st.set_page_config(page_title="Statement of Purpose Generator - ApplyBuddy", page_icon="🎓")
st.header('Statement of Purpose Generator')
st.markdown(
    """
    Unlock Your Potential with Our Statement of Purpose Generator!
    
    Crafting a compelling statement of purpose is crucial for standing out in the competitive graduate school admissions
    process. Our Statement of Purpose Generator is your go-to tool to create a captivating essay that showcases your
    unique qualities, accomplishments, and aspirations.
    """
)

st.divider()

st.markdown(
    """
    Fill out the form below to generate a personalized statement of purpose that will impress admissions committees and
    increase your chances of acceptance to your dream schools.
    """
)

# Input fields
program_and_university = st.text_input("Program and university of choice")
st.caption("Examples: Master of Science in Computer Science at Stanford University, etc.")

career_objectives = st.text_area("Career objectives")
st.caption("Examples: I am passionate about Computer Science because...")

reason_for_choosing_the_program = st.text_area("Reason for choosing the program")
st.caption("Examples: I am interested in this program because...")

academic_background = st.text_area("Academic background")
st.caption("Examples: I have achieved a GPA of 4.0...")

professional_experience = st.text_area("Professional experience")
st.caption("Examples: I have worked as a software engineer at...")

skills_and_qualities = st.text_area("Skills and qualities")
st.caption("Examples: I am a hardworking and diligent individual...")

research_interests = st.text_area("Research interests")
st.caption("Examples: I am interested in the field of...")

contribution_to_the_university = st.text_area("Contribution to the university")
st.caption("Examples: I will contribute to the university by...")

word_limit = st.number_input("Word limit", min_value=100, max_value=1000, value=500, step=100)
st.caption("The approximate number of words you want your statement of purpose to be.")

# Submit button
if not openai_api_key or openai_api_key == "":
    st.warning("Please enter your OpenAI API key in the **[Settings](/Settings)** page to submit.", icon="🚨")
elif st.button("Generate Statement of Purpose"):
    # Validate input
    if not program_and_university or program_and_university == "":
        st.warning("Please enter your program and university of choice.", icon="🚨")
    elif not career_objectives or career_objectives == "":
        st.warning("Please enter your career objectives.", icon="🚨")
    elif not reason_for_choosing_the_program or reason_for_choosing_the_program == "":
        st.warning("Please enter your reason for choosing the program.", icon="🚨")
    elif not academic_background or academic_background == "":
        st.warning("Please enter your academic background.", icon="🚨")
    elif not professional_experience or professional_experience == "":
        st.warning("Please enter your professional experience.", icon="🚨")
    elif not skills_and_qualities or skills_and_qualities == "":
        st.warning("Please enter your skills and qualities.", icon="🚨")
    elif not research_interests or research_interests == "":
        st.warning("Please enter your research interests.", icon="🚨")
    elif not contribution_to_the_university or contribution_to_the_university == "":
        st.warning("Please enter your contribution to the university.", icon="🚨")
    elif not word_limit or word_limit == "":
        st.warning("Please enter your word limit.", icon="🚨")
    else:
        # Initialize generator
        generator = StatementOfPurposeGenerator(openai_api_key, model="gpt-3.5-turbo")

        # Generate statement of purpose
        with st.spinner("Generating..."):
            args = {
                "program_and_university": program_and_university,
                "career_objectives": career_objectives,
                "reason_for_choosing_the_program": reason_for_choosing_the_program,
                "academic_background": academic_background,
                "professional_experience": professional_experience,
                "skills_and_qualities": skills_and_qualities,
                "research_interests": research_interests,
                "contribution_to_the_university": contribution_to_the_university,
                "word_limit": word_limit
            }
            statement_of_purpose = generator.generate(**args)

        # Output statement of purpose
        st.subheader("Statement of Purpose")
        st.write(statement_of_purpose)
