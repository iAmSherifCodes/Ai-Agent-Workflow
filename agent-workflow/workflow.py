import os
from crewai import Crew as CrewaiCrew, Task
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.llms import Ollama
from research_agent import research_agent
from writer_agent import writer_agent
from examiner_agent import examiner_agent

ollama_llm = Ollama(model="openhermes")
search_tool = DuckDuckGoSearchRun()

researcher = research_agent(True,False,[search_tool],ollama_llm)
writer = writer_agent(True,False,[search_tool],ollama_llm)
examiner= examiner_agent(True,False,[search_tool],ollama_llm)

topic= input("Enter your subject:  ")

task1 = Task(
    description=f'Conduct a detailed exploration of what {topic} is, delving into specific areas that can be '
                'presented in an informative and engaging manner to a broad audience',
    # description='Develop ideas for teaching someone new to the technology',
    agent=researcher,
)

task2 = Task(
    description=f'Create a 3 paragraphs long blog post about introduction to {topic} using your insights. Make it interesting, '
                         'clear and suited for everyone including a non-tech person.',
    # description=f"Use the Researcher's ideas to write a piece of text to explain the {topic}",
             agent=writer)

task3 = Task(
    # description="""
            # Create 2-3 test questions to assess the reader's understanding of the written content on the explored technology concepts""",
             description="Craft 2-3 test questions to evaluate understanding of the created text, along with the correct answers",
             agent=examiner)

crew = CrewaiCrew(
    agents=[researcher, writer, examiner],
    tasks=[task1, task2, task3],
    verbose=2
)



print("==================BEFORE===============>")

print(crew.kickoff())

print("===================AFTER===============>")