from crewai import Agent, Crew, Task, Process
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.6)

def create_branding_crew():
    agent = Agent(
        role="Brand Identity Expert",
        goal="Develop complete corporate and product brands",
        backstory="Expert in corporate branding and identity systems.",
        verbose=True,
        llm=llm
    )
    task = Task(
        description="Create full brand guidelines and identity kit.",
        expected_output="Professional brand strategy document with color system and tone of voice.",
        agent=agent
    )
    return Crew(agents=[agent], tasks=[task], process=Process.sequential, verbose=1)
