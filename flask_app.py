from flask import Flask, render_template, request
import sqlite3
import pickle
import sklearn
import os


app = Flask(__name__)

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
database_location = os.path.join(THIS_FOLDER, 'assembly_performance.db')
model_location = os.path.join(THIS_FOLDER, 'Model.pkl')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/overview')
def overview():
    return render_template('overview.html')


@app.route('/explore', methods=['GET', 'POST'])
def explore():
    if request.method == 'GET':
        return render_template('explore.html')
    if request.method == 'POST':
        constructionType = request.form["constructionType"]
        carbonFootprint = request.form["carbonFootprint"]
        databaseConnection = sqlite3.connect(database_location)
        databaseCursor = databaseConnection.cursor()
        if constructionType == "None":
            carbonFootprint = carbonFootprint.split("-")
            data = databaseCursor.execute(
                "SELECT name,assemblyTotalEC,constructionType,detail FROM wallsystem2 WHERE assemblyTotalEC BETWEEN ? AND ? ORDER BY assemblyTotalEC ASC", (carbonFootprint[0], carbonFootprint[1]))
            data = data.fetchall()
            databaseConnection.close()
            return render_template('explore.html', carbonFootprint=carbonFootprint, data=data)
        if carbonFootprint == "None":
            if constructionType[len(constructionType)-1] == '0':
                detail_no = "10"
            else:
                detail_no = constructionType[len(constructionType)-1]
            data = databaseCursor.execute(
                "SELECT name,assemblyTotalEC,constructionType,detail FROM wallsystem2 WHERE detail LIKE '" + detail_no + ".%' ORDER BY assemblyTotalEC ASC")
            data = data.fetchall()
            databaseConnection.close()
            return render_template('explore.html', constructionType=constructionType, data=data)
        else:
            carbonFootprint = carbonFootprint.split("-")
            if constructionType[len(constructionType)-1] == '0':
                detail_no = "10"
            else:
                detail_no = constructionType[len(constructionType)-1]
            data = databaseCursor.execute(
                "SELECT name,assemblyTotalEC,constructionType,detail FROM wallsystem2 WHERE detail LIKE '" + detail_no + ".%' AND assemblyTotalEC BETWEEN ? AND ? ORDER BY assemblyTotalEC ASC", (carbonFootprint[0], carbonFootprint[1]))
            data_existing = False
            for i in data:
                if data_existing == False:
                    data_existing = True
                    break
            return render_template('explore.html', carbonFootprint=carbonFootprint, constructionType=constructionType, data=data, data_existing=data_existing)


@ app.route('/detail/<id>')
def detail(id):
    databaseConnection = sqlite3.connect(database_location)
    databaseCursor = databaseConnection.cursor()
    data = databaseCursor.execute(
        "SELECT * FROM wallsystem2 WHERE detail = ?", (id,))
    data = data.fetchall()
    max_ec = 0
    for i in data:
        if i[9] != 'N/A':
            if i[9] > max_ec:
                max = i
                max_ec = i[9]
    return render_template('detail.html', data=data, id=id, max=max)


@ app.route('/analysis/<id>', methods=['POST', 'GET'])
def analysis(id):
    if request.method == "GET":
        return render_template('analysis.html', id=id)
    if request.method == "POST":
        backpan = request.form['backpan']
        r_value = request.form['r_value']
        with open(model_location, 'rb') as f:
            data = pickle.load(f)
        value = data.predict([[float(backpan), float(r_value)]])
        value = str(value[0])+' kgCO2e/m2'
        print(value)
        return render_template('analysis.html', id=id, value=value, backpan=backpan, r_value=r_value)


@ app.route('/predictor')
def predictor():
    databaseConnection = sqlite3.connect(database_location)
    databaseCursor = databaseConnection.cursor()
    data = []
    for i in range(1, 11):
        data.append(databaseCursor.execute(
            "SELECT DISTINCT name FROM wallsystem2 WHERE detail LIKE '" + str(i) + ".%'").fetchall())
    return render_template('predictor.html', data=data)


@ app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        databaseConnection = sqlite3.connect(database_location)
        databaseCursor = databaseConnection.cursor()
        window = request.form["window"]
        curtain_wall = request.form["curtain_wall"]
        balcony_roof = request.form["balcony_roof"]
        opaque_wall = request.form["opaque_wall"]
        roofing = request.form["roofing"]
        window_data = databaseCursor.execute(
            "SELECT DISTINCT constructionType,assemblyTotalEC FROM wallsystem2 WHERE name = ?", (window,)).fetchone()
        curtain_wall_data = databaseCursor.execute(
            "SELECT DISTINCT constructionType,assemblyTotalEC FROM wallsystem2 WHERE name = ?", (curtain_wall,)).fetchone()
        balcony_roof_data = databaseCursor.execute(
            "SELECT DISTINCT constructionType,assemblyTotalEC FROM wallsystem2 WHERE name = ?", (balcony_roof,)).fetchone()
        opaque_wall_data = databaseCursor.execute(
            "SELECT DISTINCT constructionType,assemblyTotalEC FROM wallsystem2 WHERE name = ?", (opaque_wall,)).fetchone()
        roofing_data = databaseCursor.execute(
            "SELECT DISTINCT constructionType,assemblyTotalEC FROM wallsystem2 WHERE name = ?", (roofing,)).fetchone()
        ec = [
            window_data[1],
            curtain_wall_data[1],
            balcony_roof_data[1],
            opaque_wall_data[1],
            roofing_data[1]
        ]
        print(ec)
        index_min = min(range(len(ec)), key=ec.__getitem__)
        if index_min == 0:
            max_ec_key = "Window"
        elif index_min == 1:
            max_ec_key = "Curtain Wall"
        elif index_min == 2:
            max_ec_key = "Balcony/Roof"
        elif index_min == 3:
            max_ec_key = "Opaque Wall"
        elif index_min == 4:
            max_ec_key = "Roofing"
        index_max = max(range(len(ec)), key=ec.__getitem__)
        if index_max == 0:
            min_ec_key = "Window"
        elif index_max == 1:
            min_ec_key = "Curtain Wall"
        elif index_max == 2:
            min_ec_key = "Balcony/Roof"
        elif index_max == 3:
            min_ec_key = "Opaque Wall"
        elif index_max == 4:
            min_ec_key = "Roofing"
        max_ec = max(ec)
        min_ec = min(ec)
        return render_template('predict.html', window_data=window_data, curtain_wall_data=curtain_wall_data, balcony_roof_data=balcony_roof_data, opaque_wall_data=opaque_wall_data, roofing_data=roofing_data, max_ec=max_ec, max_ec_key=max_ec_key, min_ec=min_ec, min_ec_key=min_ec_key)


if __name__ == '__main__':
    app.run(debug=True)
