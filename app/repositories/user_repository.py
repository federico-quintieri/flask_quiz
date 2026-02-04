from app.models import User

def get_user_by_login(login):
    return User.query.filter_by(login=login).first()

def get_user_by_nickname(nickname):
    return User.query.filter_by(nickname=nickname).first()
