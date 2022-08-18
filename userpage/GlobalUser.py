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
