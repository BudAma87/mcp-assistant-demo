# MCP Assistant (CodeCrunch Demo)

This is a simple demo application showcasing the use of the **Model Context Protocol (MCP)** with tools and a web-based UI.

## 🧠 Features
- MCP-style tool interface via FastAPI
- Calculator tool (`/tool/calculate`)
- Knowledge base tool (`/tool/knowledge`)
- Simple HTML + JavaScript frontend

## 🚀 How to Run

### 1. Install dependencies

```bash
pip install fastapi uvicorn
```

### 2. Run the MCP server

```bash
uvicorn mcp_server:app --reload
```

### 3. Open the app

Visit: [http://localhost:8000](http://localhost:8000)

### 4. Try it out

Ask:
- `calculate 25 * 4`
- `what is mcp`

## 🧱 Folder Structure

```
mcp_assistant_simple/
├── main.py
├── mcp_server.py
├── tools/
│   ├── calculator.py
│   └── kb_tool.py
├── static/
│   └── index.html
└── README.md
```

## 📚 Credits
Built for the CodeCrunch Event — LLM + MCP Exploration 🚀