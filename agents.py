from crewai import Agent, LLM
from dotenv import load_dotenv
import os

load_dotenv()

llm = LLM(
    model="groq/llama-3.1-8b-instant",
    temperature=0.3,
    api_key=os.getenv("GROQ_API_KEY")
)


researcher = Agent(
    role="Research Analyst",
    goal="Research the given topic thoroughly",
    backstory="Expert researcher skilled at collecting accurate insights.",
    llm=llm,
    verbose=True
)

summarizer = Agent(
    role="Summarizer",
    goal="Summarize research findings",
    backstory="Specialist in condensing complex information.",
    llm=llm,
    verbose=True
)

writer = Agent(
    role="Writer",
    goal="Write a structured final report",
    backstory="Professional technical writer.",
    llm=llm,
    verbose=True
)
