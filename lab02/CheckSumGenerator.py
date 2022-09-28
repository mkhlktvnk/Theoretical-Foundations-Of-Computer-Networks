import binascii
import hashlib


class CheckSumGenerator:
    def __init__(self, data: str):
        self.__data = data

    def generate(self) -> str:
        return str(hashlib.md5(binascii.unhexlify(self.__data)).hexdigest())
