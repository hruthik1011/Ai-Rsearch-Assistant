## AI Research Assistant

# Project Objective

Build an AI system where multiple AI agents collaborate to:

1)Research a topic

2)Summarize findings

3)Generate a structured final report

This mimics real-world autonomous AI teams.

# Real-World Use Case

Market research automation

Technical report generation

Academic topic exploration

Consulting-style research workflows

# Tech Stack
| Component         | Tool               |
| ----------------- | ------------------ |
| LLM               | **Groq (LLaMA-3)** |
| Agent Framework   | **CrewAI**         |
| LLM Orchestration | **LangChain**      |
| Language          | Python             |
| Environment       | Local / VS Code    |


# System Architecture
User Topic
   ↓
Research Agent → collects information
   ↓
Summarizer Agent → condenses insights
   ↓
Writer Agent → generates final report

# Project structure
ai-research-assistant/
│
├── agents.py      # Agent definitions
├── tasks.py       # Task assignments
├── main.py        # Crew execution
├── .env           # API keys
├── requirements.txt
└── README.md

# Setup Instructions
1️⃣ Clone Repository
git clone https://github.com/your-username/ai-research-assistant.git
cd ai-research-assistant

2️⃣ Create Virtual Environment
python -m venv .venv
.venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Configure API Key

Create .env:

GROQ_API_KEY=your_groq_api_key

5️⃣ Run the Project
python main.py

# Example

# Input

Generative AI applications in healthcare


# Output

Research findings

Summarized insights

Final structured report

# Future Enhancements

Web search integration

PDF report export

Streamlit UI

Vector memory (FAISS)

Deployment on Hugging Face

# Why This Project Matters

This project demonstrates:

Agent-based AI systems

Real-world LLM orchestration

Debugging production AI issues

Modern GenAI tooling
