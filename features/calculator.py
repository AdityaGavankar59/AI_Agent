import ast
import operator

# Safe operators
OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
}

def _eval(node):
    if isinstance(node, ast.Num):  # Python <=3.7
        return node.n
    if isinstance(node, ast.Constant):  # Python 3.8+
        return node.value
    if isinstance(node, ast.BinOp):
        left = _eval(node.left)
        right = _eval(node.right)
        op_type = type(node.op)
        if op_type not in OPS:
            raise ValueError("Unsupported operator")
        return OPS[op_type](left, right)
    if isinstance(node, ast.UnaryOp):
        operand = _eval(node.operand)
        op_type = type(node.op)
        if op_type not in OPS:
            raise ValueError("Unsupported unary operator")
        return OPS[op_type](operand)
    raise ValueError("Unsupported expression")

def calculate(expr: str) -> str:
    try:
        node = ast.parse(expr, mode="eval").body
        result = _eval(node)
    except Exception as e:
        return f"Could not evaluate expression: {e}"
    return f"Result: {result}"
