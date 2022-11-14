import random
from threading import Event

from accessify import private
from serial import Serial

from ChannelStatus import ChannelStatus
from ChanelStatusGenerator import ChanelAccessGenerator
from CollisionStatusGenerator import CollisionStatusGenerator
from Response import Response
from ResultStatus import ResultStatus


class Transmitter:
    def __init__(self, port_name: str, free_channel_probability: int = 0, collision_appearance_probability: int = 0):
        self.__port_name = port_name
        self.__port = Serial(port_name, 9600)
        self.__channel_status_generator = ChanelAccessGenerator(free_channel_probability)
        self.__collision_status_generator = CollisionStatusGenerator(collision_appearance_probability)

    def send_package(self, byte: str) -> Response:
        attempts_count = 0
        while True:
            if self.__channel_status_generator.generate_channel_access() == ChannelStatus.FREE:
                self.__port.write(byte.encode('cp1251'))
                k = self.generate_k(attempts_count)
                r = self.generate_r(k)
                Event().wait(r / 1000)
                if self.__collision_status_generator.is_collision_occurred():
                    attempts_count += 1
                    k = self.generate_k(attempts_count)
                    r = self.generate_r(k)
                    Event().wait(r / 1000)
                    if k >= 10:
                        return Response(ResultStatus.ERROR)
                else:
                    return Response(ResultStatus.OK)
            else:
                continue

    @private
    def generate_k(self, attempts_count: int):
        return min(attempts_count, 10)

    @private
    def generate_r(self, k: int):
        return random.randint(0, 2 ** k)
