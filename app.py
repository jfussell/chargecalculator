from flask import Flask, render_template, request
from calculator import nimh
from wtforms import IntegerField
from flask_wtf import FlaskForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sakdslfsmf387&^'


class CalcForm(FlaskForm):
    capacity = IntegerField('Capacity', render_kw={"placeholder": "mAh"})
    current = IntegerField('Current', render_kw={"placeholder": "ma"})
    efficiency = IntegerField('Efficiency', default=20, render_kw={"placeholder": "mAh"})


@app.route('/', methods=['GET', 'POST'])
def homepage():
    form = CalcForm(request.form)
    if form.validate_on_submit():
        print('form submitted')
        capacity = request.form['capacity']
        current = request.form['current']
        efficiency = request.form['efficiency']
        result = nimh(int(capacity), int(current), int(efficiency))
        print(result)
        return render_template("main.html", result=result, form=form)

    return render_template("main.html", form=form)

@app.route('/faq')
def faq():
    return render_template("faq.html")


if __name__ == "__main__":
    app.run()
