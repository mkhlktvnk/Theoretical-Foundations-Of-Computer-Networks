class InvalidPackageException(Exception):
    def __init__(self, message: str):
        self.__message = message

    def get_message(self) -> str:
        return self.__message
