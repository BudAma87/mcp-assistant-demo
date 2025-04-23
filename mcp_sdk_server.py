from fastapi import FastAPI
from modelcontextprotocol.server import MCPServer
from tools.calculator_tool import CalculatorTool
from tools.knowledge_tool import KnowledgeTool

app = FastAPI()
server = MCPServer(app=app)

server.add_tool(CalculatorTool())
server.add_tool(KnowledgeTool())