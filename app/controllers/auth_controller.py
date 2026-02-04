from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required
from app.services.auth_service import register_user, login_user_service

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    error = None
    if request.method == "POST":
        result = register_user(request.form)
        if result != "ok":
            error = result
        else:
            # redirect a login
            return redirect(url_for("auth.login"))

    return render_template("register.html", error=error)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        result = login_user_service(request.form)
        if isinstance(result, str):
            error = result
        else:
            login_user(result)
            return redirect(url_for("weather.home"))

    return render_template("login.html", error=error)

@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("weather.home"))
