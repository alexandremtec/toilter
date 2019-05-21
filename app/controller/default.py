from app import app, lm
from flask import render_template, flash, redirect, url_for
from flask_login import login_user, logout_user
from app.model.forms import LoginForm
from app.model.tables import User


@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()

@app.route('/index/<user>')
@app.route("/", defaults={"user": None})
def index(user):
    return render_template('index.html', user=user)


@app.route('/login', methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            print(user)
            login_user(user)
            return redirect(url_for("index"))
            flash("Logado")
        else:
            flash("login invalido")

    return render_template('login.html', form=form)



@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))

# Exemplo de multiplas rotas
"""
@app.route('/test', defaults={'name': None})
@app.route('/test/<name>')
def test(name):
    if name:
        return "Olá, %s!" % name
    else:
        return "Olá, usuário!"
"""