from flask import Flask, render_template, request, jsonify
from calculator import calculate

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('calculator.html')

@app.route('/calculate', methods=['POST'])
def calculate_expression():
    expression = request.json.get('expression')
    result = calculate(expression)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
