class Codec:
    def __init__(self):
        self.addr_dict = dict()

    def encode(self, longUrl: str) -> str:
        value = hex(hash(longUrl))[2:8]
        self.addr_dict[value] = longUrl
        return value

    def decode(self, shortUrl: str) -> str:
        return self.addr_dict[shortUrl]