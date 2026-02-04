from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User, db
from app.repositories.user_repository import get_user_by_login, get_user_by_nickname

def register_user(form):
    login = form["login"]
    nickname = form["nickname"]
    password = form["password"]

    if get_user_by_login(login):
        return "Login già esistente"
    if get_user_by_nickname(nickname):
        return "Nickname già esistente"

    user = User(login=login, nickname=nickname, password=generate_password_hash(password))
    db.session.add(user)
    db.session.commit()
    return "ok"

def login_user_service(form):
    user = get_user_by_login(form["login"])
    if user and check_password_hash(user.password, form["password"]):
        return user
    return None
