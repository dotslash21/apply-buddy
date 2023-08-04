from langchain.chat_models import ChatOpenAI
from langchain.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate


class PersonalStatementGenerator:
    def __init__(self, openai_api_key: str, model="gpt-3.5-turbo"):
        self.llm = ChatOpenAI(
            model=model,
            temperature=0.2,
            openai_api_key=openai_api_key
        )
        self.system_message_prompt_template = SystemMessagePromptTemplate.from_template(
            """
            You are a helpful assistant, equipped with the knowledge of the user's personality, motivation, 
            unique qualities, academic achievements, extracurricular activities, and career goals. Your task is to 
            generate a compelling and personalized "personal statement" for university applications.
            
            Expected from the Language Model:
            - Engage with the user's input to understand their personality traits, such as being empathetic,
             determined, or creative.
            - Comprehend the user's motivation for pursuing a specific field of study, and the reasons behind their
             passion and interest.
            - Utilize the provided unique qualities and accomplishments to highlight the user's individuality and
             strengths.
            - Incorporate academic achievements to showcase the user's dedication and excellence in their studies.
            - Integrate extracurricular activities and experiences to demonstrate the user's well-roundedness and
             contribution to their community.
            - Present the user's career goals, emphasizing how the chosen university/college aligns with their
             aspirations.
            
            Input from the User:
            You have access to the following details provided by the user:
            - Personality traits: [List of personality traits provided by the user]
            - Motivation for chosen field of study: [User's motivation and reasons for pursuing the selected field]
            - Unique qualities and accomplishments: [User's unique qualities, achievements, and impact]
            - Academic achievements: [User's academic accolades and performance]
            - Extracurricular activities: [User's involvement in clubs, volunteer work, sports, etc.]
            - Career goals: [User's future career aspirations and objectives]
            
            Using the provided input, craft a well-structured and cohesive personal statement that showcases the 
            user's individuality, determination, and passion. Ensure that the statement portrays the user as an ideal 
            candidate for their chosen program at the university/college. Emphasize how their unique qualities, 
            academic achievements, and extracurricular experiences align perfectly with the institution's values and 
            contribute to their future career goals.
            
            Your goal is to create a powerful and persuasive narrative that leaves a lasting impression on the 
            admissions committee, demonstrating the user's potential to thrive in their academic journey at the 
            desired university/college.
            """
        )
        self.human_message_prompt_template = HumanMessagePromptTemplate.from_template(
            """
            Personality traits: {personality}
            Motivation for chosen field of study: {motivation}
            Unique qualities and accomplishments: {unique_qualities}
            Academic achievements: {academic_achievements}
            Extracurricular activities: {extracurricular_activities}
            Career goals: {career_goals}
            """
        )

    def generate(
            self,
            personality: str,
            motivation: str,
            unique_qualities: str,
            academic_achievements: str,
            extracurricular_activities: str,
            career_goals: str) -> str:
        args = {
            "personality": personality,
            "motivation": motivation,
            "unique_qualities": unique_qualities,
            "academic_achievements": academic_achievements,
            "extracurricular_activities": extracurricular_activities,
            "career_goals": career_goals
        }
        system_message_prompt = self.system_message_prompt_template.format()
        human_message_prompt = self.human_message_prompt_template.format(**args)

        return self.llm([system_message_prompt, human_message_prompt]).content
