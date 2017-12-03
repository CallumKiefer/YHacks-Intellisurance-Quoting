import math
from sklearn import linear_model
from sklearn.externals import joblib

def get_data(age, longitude, *pre_existing):
    longitude = int(longitude)
    age = int(age)

    cond = {}
    if pre_existing[0] == "on":
        cond["R04.2"] = 1.
    else:
        cond["R04.2"] = 0.

    if pre_existing[1] == "on":
        cond["F14.121"] = 3.
    else:
        cond["F14.121"] = 0.

    if pre_existing[2] == "on":
        cond["R00.0"] = 1.
    else:
        cond["R00.0"] = 0.

    if pre_existing[3] == "on":
        cond["R19.7"] = 1.
    else:
        cond["R19.7"] = 0.

    if pre_existing[4] == "on":
        cond["M05.10"] = 3.
    else:
        cond["M05.10"] = 0.

    reg = joblib.load("plan_multiple_reg.pkl")
    plan_multiple = reg.predict([age, cond["R04.2"], \
        cond["F14.121"], cond["R19.7"], longitude])

    reg = joblib.load("personal_risk_reg.pkl")
    personal_risk = reg.predict([plan_multiple, age])

    return [(math.ceil((personal_risk + plan_multiple)*100)/100, "Bronze"), \
            (math.ceil((personal_risk + plan_multiple * 3)*100)/100, "Silver"), \
            (math.ceil((personal_risk + plan_multiple * 6)*100)/100, "Gold"), \
            (math.ceil((personal_risk + plan_multiple * 10)*100)/100, "Platinum")]
