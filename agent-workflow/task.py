# #from crewai import Agent, Task


# class Tasksy:
#     def __init__(self) -> None:
#         self.research_task()
#         self.writer_task()
#         self.examiner_task()

#     def research_task(agent:Agent):
#         return Task(
#                 # description='Conduct a detailed exploration of what technology is, delving into specific areas that can be '
#                     # 'presented in an informative and engaging manner to a broad audience',
#             description='Develop ideas for teaching someone new to the technology',
#             agent=agent,
#         )

#     def writer_task(agent:Agent):
#         return Task(
#                 # description='Create a 3 paragraphs long blog post about introduction to technology using your insights. Make it interesting, '
#                             #  'clear and suited for everyone including a non-tech person.',
#             description="Use the Researcher's ideas to write a piece of text to explain the topic",
#             agent=agent,
#         )

#     def examiner_task(agent:Agent):
#         return Task(
#             # description="""
#                 # Create 2-3 test questions to assess the reader's understanding of the written content on the explored technology concepts""",
#             description="Craft 2-3 test questions to evaluate understanding of the created text, along with the correct answers",
#             agent=agent
#         )