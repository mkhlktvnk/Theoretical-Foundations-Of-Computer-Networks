from enum import Enum


class Response:
    def __init__(self, status: Enum, data: str = ''):
        self.__status = status
        self.__data = data

    def get_status(self) -> Enum:
        return self.__status

    def get_data(self) -> str:
        return self.__data

