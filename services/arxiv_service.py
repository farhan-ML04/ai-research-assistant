import requests

def search_papers(query):
    url = f"http://export.arxiv.org/api/query?search_query=all:{query}&start=0&max_results=5"
    
    response = requests.get(url).text

    return response