from flask import Flask, request, jsonify
from flask_cors import CORS

import main

app = Flask(__name__)
app.config['ENV'] = 'development'
app.config['DEBUG'] = True

CORS(app, resources=r'/*')

@app.route('/author=wongxy', methods=['GET', 'POST'])
def bili_cover():
    data = request.json
    if data:
        data = dict(data)
        t = data.get('t')
        url = data.get('url')
        return main.get(t, url)
    return {'msg': 'missing data'}


if __name__ == "__main__":
    app.run()