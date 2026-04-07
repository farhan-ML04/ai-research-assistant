from utils.llm import get_llm

def summarizer_agent(papers):
    model = get_llm()

    prompt = f"""
    Summarize the following research data into key points:

    {papers}
    """

    return model.generate_content(prompt).text