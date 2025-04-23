from modelcontextprotocol import Tool, ToolInput, ToolOutput

knowledge_base = {
    "mcp": "Model Context Protocol enables LLMs to use tools reliably.",
    "rag": "RAG stands for Retrieval-Augmented Generation. It lets LLMs fetch external info.",
    "llm": "Large Language Models like Claude or GPT generate human-like responses."
}

class KnowledgeInput(ToolInput):
    term: str

class KnowledgeOutput(ToolOutput):
    result: str

class KnowledgeTool(Tool):
    name = "knowledge"
    description = "Answers simple AI-related terms like 'MCP', 'RAG', etc."

    def run(self, input: KnowledgeInput) -> KnowledgeOutput:
        return KnowledgeOutput(result=knowledge_base.get(input.term.lower(), "Not found."))