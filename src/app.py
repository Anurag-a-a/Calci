from flask import Flask, jsonify, request

app = Flask(__name__)

class Calculator:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def subtract(a, b):
        return a - b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
@app.route('/')
def home():
    return "Welcome to the Calculator API!"

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    operation = data.get('operation')
    num1 = data.get('num1')
    num2 = data.get('num2')

    try:
        if operation == 'add':
            result = Calculator.add(num1, num2)
        elif operation == 'subtract':
            result = Calculator.subtract(num1, num2)
        elif operation == 'multiply':
            result = Calculator.multiply(num1, num2)
        elif operation == 'divide':
            result = Calculator.divide(num1, num2)
        else:
            return jsonify({"error": "Invalid operation"}), 400

        return jsonify({"result": result})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)