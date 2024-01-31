from crewai import Crew

class CrewSetUp:

    def __init__(self) -> None:
        pass

    def crew(agents: list, tasks: list, verbose: int):
        return Crew(
            agents=agents,
            tasks=tasks,
            verbose=verbose
        )
    