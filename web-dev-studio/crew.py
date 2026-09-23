from crewai import Agent, Crew, Task, Process
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)

def create_webdev_crew():
    agent = Agent(
        role="Senior Full-Stack Developer",
        goal="Build production-grade web and mobile applications",
        backstory="Expert in Next.js, React, Node.js, Flutter and modern full-stack development.",
        verbose=True,
        llm=llm
    )
    task = Task(
        description="Generate complete, clean, production-ready full-stack web and mobile app code.",
        expected_output="Full codebase with folder structure, README, and deployment instructions.",
        agent=agent
    )
    return Crew(agents=[agent], tasks=[task], process=Process.sequential, verbose=1)
