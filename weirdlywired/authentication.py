from datetime import timedelta
from typing import Tuple

from django.conf import settings
from django.utils import timezone
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed

from tenant.models import User


def expires_in(token: Token) -> timedelta:
    """"""
    time_elapsed = timezone.now() - token.created
    return timedelta(seconds=settings.EXPIRE_TOKEN_AFTER_SECONDS) - time_elapsed


def is_token_expired(token: Token):
    """"""
    return expires_in(token=token) < timedelta(seconds=0)


def token_expire_handler(token: Token) -> Tuple[bool, Token]:
    """
    TO BE CALLED BY LOGIN API ONLY
    If token is expired new token will be established
    If token is expired then it will be removed
    and new one with different key will be created
    """
    is_expired = is_token_expired(token)
    if is_expired:
        token.delete()
        token = Token.objects.create(user=token.user)
    return (is_expired, token)


def verify_token_key(key: str) -> Tuple[User, Token]:
    try:
        token = Token.objects.get(key=key)
    except Token.DoesNotExist:
        raise AuthenticationFailed("TOKEN_INVALID")

    if not token.user.is_active:
        raise AuthenticationFailed("USER_INACTIVE")

    if is_token_expired(token=token):
        raise AuthenticationFailed("TOKEN_EXPIRED")

    return (token.user, token)


"""
Custom Default Authentication classes
"""


class ExpiringTokenAuthentication(TokenAuthentication):
    """
    If token is expired then it will be removed
    and new one with different key will be created
    """

    def authenticate_credentials(self, key: str) -> Tuple[User, Token]:
        return verify_token_key(key=key)
