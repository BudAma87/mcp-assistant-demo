knowledge = {
    "mcp": "Model Context Protocol is a standard that allows LLMs to interact with tools.",
    "rag": "RAG stands for Retrieval-Augmented Generation. It allows LLMs to fetch information."
}

def lookup(term: str) -> str:
    return knowledge.get(term.lower(), "I don't know that yet.")