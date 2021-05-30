import os

from .common import Common


class Production(Common):

    # Local Env will be in DEBUG mode
    DEBUG = True
    REDIS_HOST = os.environ.get("REDIS_HOST", "")
    REDIS_PORT = os.environ.get("REDIS_PORT", "")
    CHANNEL_LAYERS = {
        "default": {
            "BACKEND": "channels_redis.core.RedisChannelLayer",
            "CONFIG": {
                "hosts": [(REDIS_HOST, REDIS_PORT)],
            },
        },
    }
