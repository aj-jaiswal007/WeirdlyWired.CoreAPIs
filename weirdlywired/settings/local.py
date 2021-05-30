from .common import Common


class Local(Common):

    # Local Env will be in DEBUG mode
    DEBUG = True

    # Django channel
    CHANNEL_LAYERS = {"default": {"BACKEND": "channels.layers.InMemoryChannelLayer"}}
