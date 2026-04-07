from utils.llm import get_llm

def analyst_agent(summary):
    model = get_llm()

    prompt = f"""
    Analyze the summary and provide:
    - Key insights
    - Trends
    - Research gaps

    {summary}
    """

    return model.generate_content(prompt).text