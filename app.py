from flask import Flask, request, jsonify
from flask_cors import CORS

import bilibili_cover


app = Flask(__name__)
app.config.from_pyfile('config.py')

CORS(app, resources=r'/*')

@app.route('/bilibili_cover', methods=['GET', 'POST'])
def bili_cover():
    data = request.json
    if data:
        print(data)
        url = data['url']
        if url:
            return jsonify(bilibili_cover.get(url))
    return jsonify({"msg":"missing data"})



if __name__ == "__main__":
    app.run()