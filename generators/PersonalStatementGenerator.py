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
            You are a helpful assistant, and I appreciate your guidance in crafting a compelling personal 
            statement for my university application. Here are the key inputs:

            1. University: [Name of University]
            2. Field of Study: [Field of Study]
            3. Personal Motivation: [Reason for choosing this field and university]
            4. Personality Traits: [Brief description of my personality traits]
            5. Strengths and Weaknesses: [Candid reflection on my strengths and weaknesses]
            6. Interests and Hobbies: [My interests and hobbies]
            7. Relevant Skills and Experiences: [Skills and experiences gained so far]
            8. Academic Achievements: [My academic achievements]
            9. Extracurricular Activities: [My involvement in extracurriculars]
            10. Future Career Goals: [My aspirations for the future]
            11. Word Limit: [Word limit for the personal statement]

            Now, I trust you to weave these inputs into a concise and engaging narrative that reflects my persona, 
            aspirations, and potential contributions to the university community. Remember to showcase honesty, 
            authenticity, and creativity while presenting my experiences and future goals.
            """
        )
        self.human_message_prompt_template = HumanMessagePromptTemplate.from_template(
            """
            University: {university}
            Field of Study: {field_of_study}
            Personal Motivation: {motivation}
            Personality Traits: {personality}
            Strengths and Weaknesses: {strengths_and_weaknesses}
            Interests and Hobbies: {interests_and_hobbies}
            Relevant Skills and Experiences: {skills_and_experiences}
            Academic Achievements: {academic_achievements}
            Extracurricular Activities: {extracurricular_activities}
            Future Career Goals: {career_goals}
            Word Limit: {word_limit}
            """
        )

    def generate(self, **kwargs) -> str:
        system_message_prompt = self.system_message_prompt_template.format()
        human_message_prompt = self.human_message_prompt_template.format(**kwargs)

        return self.llm([system_message_prompt, human_message_prompt]).content
