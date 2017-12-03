import zipcode
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash
import regression_file

app = Flask(__name__)  # create the application instance :)
app.config.from_object(__name__)  # load config from this file , flaskr.py

@app.route(r'/')
def landingpage_with_survey():
    return render_template('index2.html')

@app.route(r'/processing', methods=["POST"])
def gettingdata():
    gender = request.form.get("gender")
    city = request.form.get("city")
    zip = request.form.get("zip")
    zip = zipcode.isequal(zip)
    lat = zip.lat
    lon = zip.lon
    height = request.form.get("height")
    smoke = request.form.get("smoke")
    age = request.form.get("age")
    state = request.form.get("states")
    weight = request.form.get("weight")
    income = request.form.get("income")
    coverage = request.form.get("coverage")
    married_status = request.form.get("married_status")
    try:
        opinsured = request.form.get("500k")
    except:
        opinsured = int(request.form.get("other"))
    pre_existing = []
    try:
        pre_existing.append(request.form.get("c1"))
    except:
        pass
    try:
        pre_existing.append(request.form.get("c2"))
    except:
        pass
    try:
        pre_existing.append(request.form.get("c3"))
    except:
        pass
    try:
        pre_existing.append(request.form.get("c4"))
    except:
        pass
    try:
        pre_existing.append(request.form.get("c5"))
    except:
        pass
    regression_file.get_data(age, lon, *pre_existing)
    # model_training.get_data(city, age, lon, gender, state, lat, coverage, opinsured, income, married_status, height, weight, smoke, *pre_existing)
    return "yay"


if __name__ == '__main__':
    # import model_training
    app.run()
