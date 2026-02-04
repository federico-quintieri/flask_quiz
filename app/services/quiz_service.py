from app.repositories.quiz_repository import get_random_question, get_question_by_id
from app.models import db, User

def fetch_random_question():
    """Ritorna una domanda casuale"""
    return get_random_question()

def check_answer(user: User, question_id: int, selected_answer: int):
    """
    Controlla la risposta e aggiorna il punteggio dell'utente se corretta.
    Ritorna True se corretto, False altrimenti.
    """
    question = get_question_by_id(question_id)
    if not question:
        return False

    if selected_answer == question.correct:
        user.score += 1
        db.session.commit()
        return True
    return False
