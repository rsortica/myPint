# criar as views (rotas/links) do site
from flask import render_template, url_for
from myPinterest import app
from flask_login import login_required

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/profile/<usuario>")
@login_required
def perfil(usuario):
    return render_template("profile.html", usuario=usuario)