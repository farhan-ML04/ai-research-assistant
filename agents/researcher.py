from services.arxiv_service import search_papers

def research_agent(topic):
    papers = search_papers(topic)
    return papers