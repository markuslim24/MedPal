from flask_wtf import FlaskForm
from wtforms import DecimalField
from wtforms.validators import DataRequired


class ABGInterpreterForm(FlaskForm):
    ph = DecimalField("ph", validators=[DataRequired()])
    paco2 = DecimalField("paco2", validators=[DataRequired()])
    hco3 = DecimalField("hco3", validators=[DataRequired()])
    na = DecimalField("na", validators=[DataRequired()])
    cl = DecimalField("cl", validators=[DataRequired()])
    mso = DecimalField("mso", validators=[DataRequired()])
    glu = DecimalField("glu", validators=[DataRequired()])
    urea = DecimalField("urea", validators=[DataRequired()])
