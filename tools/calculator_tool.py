from modelcontextprotocol import Tool, ToolInput, ToolOutput

class CalculatorInput(ToolInput):
    expression: str

class CalculatorOutput(ToolOutput):
    result: str

class CalculatorTool(Tool):
    name = "calculator"
    description = "Evaluates math expressions like '5 * 3 + 2'"

    def run(self, input: CalculatorInput) -> CalculatorOutput:
        try:
            result = eval(input.expression)
            return CalculatorOutput(result=str(result))
        except Exception as e:
            return CalculatorOutput(result=f"Error: {e}")