from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import FingerTraining
from . import db
import json

views = Blueprint("views", __name__)

@views.route("/", methods=["GET", "POST"])
@login_required
def home():
    if request.method == "POST":
        hang = request.form.get("hang", type=int)
        rest = request.form.get("rest")
        train_set = request.form.get("train_set")
        weight = request.form.get("weight")
        if not hang or not rest or not train_set or not weight:
            flash("Please fill the blank block", category="error")
        else:
            new_finger_training = FingerTraining(hang=hang, rest=rest, train_set=train_set, weight=weight, user_id=current_user.id)
            db.session.add(new_finger_training)
            db.session.commit()
            flash("Record added!", category="success")
    
    return render_template("home.html", user=current_user)

@views.route("/delete_finger_training", methods=["POST"])
@login_required
def delete_finger_training():
    data = json.loads(request.data)
    finger_training_id = data["finger_training_id"]
    finger_training = FingerTraining.query.get(finger_training_id)
    if finger_training.user_id == current_user.id:
        db.session.delete(finger_training)
        db.session.commit()
        return jsonify({})
    