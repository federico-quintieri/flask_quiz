from app.models import Quiz

def get_random_question():
    """Ritorna una domanda casuale dal DB"""
    from random import choice
    all_questions = Quiz.query.all()
    if not all_questions:
        return None
    return choice(all_questions)

def get_question_by_id(question_id):
    """Ritorna la domanda con l'id specificato"""
    return Quiz.query.get(question_id)
