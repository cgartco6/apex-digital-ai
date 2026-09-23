from crewai import Agent, Crew, Task, Process
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)

def create_marketing_crew():
    agent = Agent(
        role="Inbound Marketing Expert",
        goal="Create pure pull marketing strategies",
        backstory="Expert in SEO, content marketing, and organic customer acquisition.",
        verbose=True,
        llm=llm
    )
    task = Task(
        description="Create complete inbound marketing strategy and playbook.",
        expected_output="90-day marketing playbook with SEO, content calendar and tactics.",
        agent=agent
    )
    return Crew(agents=[agent], tasks=[task], process=Process.sequential, verbose=1)
