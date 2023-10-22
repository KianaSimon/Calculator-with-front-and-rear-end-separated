from flask import Flask, request, jsonify
import math
import tkinter
import tkinter as tk
import numpy as np
import re
import sqlite3

app = Flask(__name__)
@app.route('/')
def index():
    return app.send_static_file('cal.html')

@app.route('/process-text', methods=['POST'])

def process_text():
    data = request.json
    text_all = data.get('text')
    print('Received text:', text_all)
    try:
        result = re.sub(r'(sin|cos|tan|pi|e)\b', r'math.\1', text_all)
        result = re.sub(r'ln', 'np.log', result)
        result = re.sub(r'lg', 'np.log10', result)
        result = re.sub(r'\^', '**', result)
        result = re.sub(r'sqrt\((.*?)\)', r'\1**0.5', result)
        result = str(eval(result))
    except Exception as e:
        result = "error"
    return jsonify({'result': f' { result }'})


if __name__ == '__main__':
    app.run(debug=True)
