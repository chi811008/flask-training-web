from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from website.models import FingerTraining
from website import db
import json

finger_training = Blueprint("finger_training", __name__)

@finger_training.route("/finger_trainings", methods=["GET", "POST"])
@login_required
def add_finger_training():
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
    
    return render_template("finger_training.html", user=current_user)

@finger_training.route("/delete_finger_training", methods=["POST"])
@login_required
def delete_finger_training():
    data = json.loads(request.data)
    finger_training_id = data["finger_training_id"]
    finger_training = FingerTraining.query.get(finger_training_id)
    if finger_training.user_id == current_user.id:
        db.session.delete(finger_training)
        db.session.commit()
        return jsonify({})
    