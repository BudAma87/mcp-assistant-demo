from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from tools import calculator, kb_tool

app = FastAPI()

@app.get("/tool/calculate")
def run_calculator(q: str):
    return {"result": calculator.calculate(q)}

@app.get("/tool/knowledge")
def lookup(term: str):
    return {"result": kb_tool.lookup(term)}

app.mount("/", StaticFiles(directory="static", html=True), name="static")