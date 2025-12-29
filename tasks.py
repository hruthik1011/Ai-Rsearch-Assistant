from crewai import Task
from agents import researcher, summarizer, writer

research_task = Task(
    description="Research the given topic and list important points.",
    expected_output="Bullet points with factual information.",
    agent=researcher
)

summary_task = Task(
    description="Summarize the researched content into key insights.",
    expected_output="Concise summary.",
    agent=summarizer
)

writing_task = Task(
    description="Generate a detailed final report based on the summary.",
    expected_output="Structured and professional report.",
    agent=writer
)
