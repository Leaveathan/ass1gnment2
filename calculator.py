from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    expression = request.json['expression']
    result = eval(expression, {'__builtins__': None}, math.__dict__)
    history.append(expression)
    return jsonify({'result': result})

@app.route('/history')
def get_history():
    return jsonify(history)

if __name__ == '__main__':
    history = []
    app.run()
