import secrets


def get_random_key():
    return secrets.token_urlsafe(20)
