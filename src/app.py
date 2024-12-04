from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route('/calculate', methods = ['POST'])

def calculate():
    data = request.get_json()

    operation = data['operation']

    num1 = data['num1']
    num2 = data['num2']

    if operation == 'add':
        result = num1 + num2
    
    elif operation == 'subtract':
        result = num1 - num2

    elif operation == 'multiply':
        result = num1 * num2
    
    elif operation == 'divide':
        result = num1/num2 if num2 != 0 else 'Error: Divisible by zero'

    else:
        return jsonify({'error' : 'Invalid Operation'}),400
    
    return jsonify({result:result})


if __name__ == '__main__':
    app.run(debug=True)