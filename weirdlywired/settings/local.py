import os
from .common import Common


class Local(Common):

    # Local Env will be in DEBUG mode
    DEBUG = True

    # Django channel
    # CHANNEL_LAYERS = {"default": {"BACKEND": "channels.layers.InMemoryChannelLayer"}}
    # Local Env will be in DEBUG mode
    REDIS_HOST = os.environ.get("REDIS_HOST", "")
    REDIS_PORT = os.environ.get("REDIS_PORT", "")
    print("------------", REDIS_HOST, REDIS_PORT)
    CHANNEL_LAYERS = {
        "default": {
            "BACKEND": "channels_redis.core.RedisChannelLayer",
            "CONFIG": {
                "hosts": [(REDIS_HOST, REDIS_PORT)],
            },
        },
    }
