# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route("/add")
def do_add():
    """Add a and b parameters."""
    a = request.args.get("a")
    b = request.args.get("b")
    result = add(int(a), int(b))

    return str(result)

@app.route("/sub")
def do_sub():
    """Subtract and b parameters."""
    a = request.args.get("a")
    b = request.args.get("b")
    result = sub(int(a), int(b))

    return str(result)

@app.route("/mult")
def do_mult():
    """Subtract and b parameters."""
    a = request.args.get("a")
    b = request.args.get("b")
    result = mult(int(a), int(b))

    return str(result)

@app.route("/div")
def do_div():
    """Subtract and b parameters."""
    a = request.args.get("a")
    b = request.args.get("b")
    result = div(int(a), int(b))

    return str(result)
    
    
@app.route("/math/<oper>")
def do_math(oper):
    ops = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
        }
    """Do math on a and b."""

    a = request.args.get("a")
    b = request.args.get("b")
    result = ops[oper](int(a), int(b))

    return str(result)