from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/results', methods=['POST'])
def results():
    tag = request.form['tag']
    url = "https://shazam.p.rapidapi.com/search"
    querystring = {"term": tag, "locale": "en-US", "offset": "0", "limit": "20"}
    headers = {
        "X-RapidAPI-Host": "shazam.p.rapidapi.com",
        "X-RapidAPI-Key": "388751cc24msh1f87b7f0b27d26ap16b818jsn9224a0e445da"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()

    hits = data["tracks"]["hits"]

    return render_template('results.html', tracks=hits)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
