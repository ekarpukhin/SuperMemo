"""
    Глобальный пользователь
_user - для БД алгоритма
_account - в БД сайта, в него пользователь "входит", через него сайт находит _user
"""

_user = None
_account = None


def set_account(account):
    global _account
    _account = account


def get_account():
    return _account


def set_user(user):
    global _user
    _user = user


def get_user():
    return _user


def get_login_status(key):
    """ Возвращает True, если пользователь вошел в аккаунт, False в противном случае """
    if key == "user":
        if _user is not None:
            return True
        else:
            return False
    if key == "account":
        if _account is not None:
            return True
        else:
            return False


def get_username():
    if _account is not None:
        return _account.user_login
    else:
        return "None"
