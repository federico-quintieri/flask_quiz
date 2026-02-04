from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from app.services.quiz_service import fetch_random_question, check_answer

quiz_bp = Blueprint("quiz", __name__, url_prefix="/quiz")

@quiz_bp.route("/", methods=["GET", "POST"])
@login_required
def quiz():
    if request.method == "POST":
        selected = int(request.form["answer"])
        question_id = int(request.form["question_id"])
        check_answer(current_user, question_id, selected)

    question = fetch_random_question()  # domanda casuale
    return render_template("quiz.html", question=question, score=current_user.score)

@quiz_bp.route("/leaderboard")
def leaderboard():
    from app.models import User
    users = User.query.order_by(User.score.desc()).all()
    return render_template("leaderboard.html", users=users)
