from agents.researcher import research_agent
from agents.summarizer import summarizer_agent
from agents.analyst import analyst_agent
from utils.llm import get_llm

def run_research(topic):

    papers = research_agent(topic)
    summary = summarizer_agent(papers)
    analysis = analyst_agent(summary)

    model = get_llm()

    final_prompt = f"""
    Create a structured research report:

    Topic: {topic}

    Summary:
    {summary}

    Analysis:
    {analysis}

    Format nicely.
    """

    report = model.generate_content(final_prompt).text

    return report