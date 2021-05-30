class Headers:
    """DTO for websocket scope"""

    def __init__(self, scope):
        self._scope = scope

    def keys(self):
        return [header[0].decode() for header in self._scope["headers"]]

    def as_dict(self) -> dict:
        return {h[0].decode(): h[1].decode() for h in self._scope["headers"]}

    def __getitem__(self, item: str) -> str:
        return self.as_dict()[item.lower()]

    def __repr__(self) -> str:
        return str(dict(self))
