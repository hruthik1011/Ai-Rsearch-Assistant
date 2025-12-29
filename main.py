from crewai import Crew
from agents import researcher, summarizer, writer
from tasks import research_task, summary_task, writing_task

def run_research(topic):
    crew = Crew(
        agents=[researcher, summarizer, writer],
        tasks=[research_task, summary_task, writing_task],
        verbose=True
    )

    result = crew.kickoff(inputs={"topic": topic})
    return result

if __name__ == "__main__":
    topic = input("Enter research topic: ")
    output = run_research(topic)

    print("\n FINAL REPORT\n")
    print(output)
