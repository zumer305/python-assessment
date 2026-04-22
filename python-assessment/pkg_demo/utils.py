# utils.py

def safe_div(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b