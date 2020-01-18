from flask import Flask, request


app = Flask(__name__)
app.config['ENVIRONMENT'] = 'develop'

@app.route('/test/<url>', methods=['GET', 'POST'])
def test(url):
    if request.method == 'POST':
        data = request.form
        name = data.get('name')
        gender = data.get('gender')
        return f'name:{name}\ngender:{gender}'
    else:
        return url, type(url)


if __name__ == "__main__":
    app.run()