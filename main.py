from agents.coordinator import run_research

if __name__ == "__main__":
    topic = input("Enter research topic: ")
    result = run_research(topic)
    print(result)