from crewai import Agent, Crew, Task, Process
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

def create_design_crew():
    agent = Agent(role="Master Graphic Designer", goal="Create exceptional designs", backstory="World-class designer", verbose=True, llm=llm)
    task = Task(description="Create full design assets", expected_output="Design package", agent=agent)
    return Crew(agents=[agent], tasks=[task], process=Process.sequential)
