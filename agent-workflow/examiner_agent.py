from crewai import Agent

def examiner_agent(verbose:bool, allow_delegation:bool, tools:list, llm):
    return Agent(
    role='Tech Evaluation Expert',
    goal='Craft 2-3 test questions to evaluate understanding of the created text, along with the correct answers',
    backstory='You are a detail-oriented pro in educational assessment, ensuring accurate evaluation of tech knowledge',
    verbose=verbose,
    allow_delegation=allow_delegation,
    tools=tools,
    llm=llm)