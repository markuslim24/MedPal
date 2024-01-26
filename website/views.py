import re
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_wtf import FlaskForm
from .tools.abginterpreter import determine_acid_base_balance
from .forms.abgInterpreterForm import ABGInterpreterForm

views = Blueprint("views", __name__)


@views.route("/", methods=["GET", "POST"])
def home():
    global abginput
    abginput = {
        "ph": "",
        "paco2": "",
        "hco3": "",
        "na": "",
        "cl": "",
        "mso": "",
        "glu": "",
        "urea": "",
    }
    global abgresult
    abgresult = None
    abgform = ABGInterpreterForm()
    if request.method == "POST":
        ph = request.form.get("ph")
        paco2 = request.form.get("paco2")
        hco3 = request.form.get("hco3")
        na = request.form.get("na")
        cl = request.form.get("cl")
        mso = request.form.get("mso")
        glu = request.form.get("glu")
        urea = request.form.get("urea")

        if (
            len(ph) < 1
            or len(paco2) < 1
            or len(hco3) < 1
            or len(na) < 1
            or len(cl) < 1
            or len(mso) < 1
            or len(glu) < 1
            or len(urea) < 1
        ):
            flash("Please fill out all fields.", category="error")
        elif (
            not is_convertible_to_number(ph)
            or not is_convertible_to_number(paco2)
            or not is_convertible_to_number(hco3)
            or not is_convertible_to_number(na)
            or not is_convertible_to_number(cl)
            or not is_convertible_to_number(mso)
            or not is_convertible_to_number(glu)
            or not is_convertible_to_number(urea)
        ):
            flash("Please enter valid numerical values.", category="error")
        else:
            abginput["ph"] = ph
            abginput["paco2"] = paco2
            abginput["hco3"] = hco3
            abginput["na"] = na
            abginput["cl"] = cl
            abginput["mso"] = mso
            abginput["glu"] = glu
            abginput["urea"] = urea

            ph = float(ph)
            paco2 = float(paco2)
            hco3 = float(hco3)
            na = float(na)
            cl = float(cl)
            mso = float(mso)
            glu = float(glu)
            urea = float(urea)
            abgresult = determine_acid_base_balance(
                ph, paco2, hco3, na, cl, mso, glu, urea
            )
            print(abgresult)
            # return redirect(url_for("views.home"))

    return render_template(
        "home.html", abginput=abginput, abgresult=abgresult, abgform=abgform
    )


def is_convertible_to_number(input_str):
    pattern = r"^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?$"
    return bool(re.match(pattern, input_str))
