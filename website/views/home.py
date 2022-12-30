from flask import Blueprint, render_template
from flask_login import current_user

views = Blueprint("views", __name__)

@views.route("/", methods=["GET"])
def home():
    user = current_user if current_user else None
    return render_template("home.html", user=user)
