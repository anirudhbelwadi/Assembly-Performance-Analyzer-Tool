from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/overview')
def overview():
    return render_template('overview.html')


@app.route('/explore')
def explore():
    return render_template('explore.html')


@app.route('/detail')
def detail():
    return render_template('detail.html')


@app.route('/analysis')
def analysis():
    return render_template('analysis.html')


@app.route('/predictor')
def predictor():
    return render_template('predictor.html')


@app.route('/predict')
def predict():
    return render_template('predict.html')


if __name__ == '__main__':
    app.run(debug=True)
