import os
from crewai import Agent, Task, Crew
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.llms import Ollama


ollama_llm = Ollama(model="openhermes")
search_tool = DuckDuckGoSearchRun()


researcher = Agent(
    role='Senior Research Analyst in Technology',

    goal='Explore various aspects of technology, identify key concepts such as programming '
         'languages, emerging technologies, and their practical applications. Create '
         'teaching ideas that demystify complex technological topics for beginners and a non-tech person',

    backstory='You are a seasoned professional in the research field of technology, with a background in '
              'education. You are passionate about bridging the knowledge gap and making technology accessible to '
              'individuals at all levels. Your expertise ranges from software development to IT infrastructure, '
              'providing a well-rounded understanding of the subject',
    verbose=True,
    allow_delegation=False,
    tools=[search_tool],
    llm=ollama_llm
)

writer = Agent(
    role='Tech Content Strategist',
    goal='Break down complex technological concepts into easy-to-understand language, providing a narrative that '
         'engages readers and sparks their interest in the world of technology',
    backstory='You are a skilled writer with a background in technology journalism and content creation. You have a '
              'knack for turning technical jargon into relatable content, ensuring that readers, regardless of their '
              'technical background, can grasp the essence of technological advancements and their impact on society',
    verbose=True,
    allow_delegation=False,
    tools=[search_tool],
    llm=ollama_llm
)

examiner = Agent(
    role='Tech Evaluation Expert',
    goal='Craft 2-3 test questions to evaluate understanding of the created text, along with the correct answers',
    backstory='You are a detail-oriented pro in educational assessment, ensuring accurate evaluation of tech knowledge',
    verbose=True,
    allow_delegation=False,
    tools=[search_tool],
    llm=ollama_llm
)

# Delegate task to each agent

task1 = Task(
    # description='Conduct a detailed exploration of what technology is, delving into specific areas that can be '
                # 'presented in an informative and engaging manner to a broad audience',
    description='Develop ideas for teaching someone new to the technology',
    agent=researcher,
)

task2 = Task(
    # description='Create a 3 paragraphs long blog post about introduction to technology using your insights. Make it interesting, '
                        #  'clear and suited for everyone including a non-tech person.',
    description="Use the Researcher's ideas to write a piece of text to explain the topic",
             agent=writer)

task3 = Task(
    # description="""
            # Create 2-3 test questions to assess the reader's understanding of the written content on the explored technology concepts""",
             description="Craft 2-3 test questions to evaluate understanding of the created text, along with the correct answers",
             agent=examiner)

crew = Crew(
    agents=[researcher, writer, examiner],
    tasks=[task1, task2, task3],
    verbose=2
)

print("####################################")
result = crew.kickoff()
print(result)
print("####################################")
