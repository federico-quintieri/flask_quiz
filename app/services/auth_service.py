from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User, db
from app.repositories.user_repository import get_user_by_nickname


def register_user(form):
    nickname = form["nickname"]
    password = form["password"]
    conferma_password = form.get("conferma_password")

    # Controllo nickname unico
    if get_user_by_nickname(nickname):
        return "Nickname già esistente"

    # Controllo password identiche
    if password != conferma_password:
        return "Le password non coincidono"

    # Creazione utente
    user = User(nickname=nickname, password=generate_password_hash(password))
    db.session.add(user)
    db.session.commit()
    return "ok"


def login_user_service(form):
    nickname = form["nickname"]
    password = form["password"]

    user = get_user_by_nickname(nickname)

    # 1️⃣ Controllo nickname esistente
    if not user:
        return "Nickname inesistente"

    # 2️⃣ Controllo password
    if not check_password_hash(user.password, password):
        return "Password errata"

    # Login corretto
    return user
