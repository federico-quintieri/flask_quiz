from app import app
from models import Quiz , User, db

with app.app_context():
    print(Quiz.query.all())
    print(User.query.all())
    # if not Quiz.query.first():
    #     q1 = Quiz(question="Quanto fa 2+2?", option1="2", option2="3", option3="4", option4="5", correct=3)
    #     q2 = Quiz(question="Colore del cielo?", option1="Blu", option2="Verde", option3="Rosso", option4="Giallo", correct=1)
    #     db.session.add_all([q1, q2])
    #     db.session.commit()

