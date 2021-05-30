from urllib import parse


class QueryParams:
    def __init__(self, query_string: str):
        self._dict = dict(parse.parse_qsl(query_string))

    def keys(self):
        return self._dict.keys()

    def get(self, item, default=None):
        return self._dict.get(item, default)

    def __getitem__(self, item: str):
        return self._dict[item]

    def __repr__(self) -> str:
        return str(dict(self))
