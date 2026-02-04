from app.repositories.quiz_repository import get_random_question, get_question_by_id
from app.models import db, User


def fetch_random_question():
    """Ritorna una domanda casuale"""
    return get_random_question()


def check_answer(user: User, question_id: int, selected_answer: int):
    """
    Controlla la risposta e aggiorna lo score:
    +1 se corretto, -1 se sbagliato.
    """
    question = get_question_by_id(question_id)
    if not question:
        return False

    if selected_answer == question.correct:
        user.score += 1
        correct = True
    else:
        user.score -= 1
        correct = False

    db.session.commit()
    return correct
