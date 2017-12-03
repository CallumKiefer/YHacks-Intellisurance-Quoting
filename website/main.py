from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash

app = Flask(__name__)  # create the application instance :)
app.config.from_object(__name__)  # load config from this file , flaskr.py

@app.route(r'/')
def landingpage_with_survey():
    return render_template('index2.html')

@app.route(r'/processing', methods=["POST"])
def gettingdata():
    request.form["gender"]
    gender = request.form.get["gender"]
    city = request.form.get["city"]
    height = request.form.get["height"]
    smoke = request.form.get["smoke"]
    age = request.form.get["age"]
    states = request.form.get["states"]
    weight = request.form.get["weight"]
    income = request.form.get["income"]
    coverage = request.form.get["gender"]
    married_status = request.form.get["gender"]
    op1 = request.form.get["gender"]
    opother = request.form.get["gender"]
    try:
        c1 = request.form.get["c1"]
    except:
        pass
    try:
        c2 = request.form.get["c2"]
    except:
        pass
    try:
        c3 = request.form.get["c3"]
    except:
        pass
    try:
        c4 = request.form.get["c4"]
    except:
        pass
    try:
        c5 = request.form.get["c5"]
    except:
        pass
    return "yay"


if __name__ == '__main__':
    app.run()
