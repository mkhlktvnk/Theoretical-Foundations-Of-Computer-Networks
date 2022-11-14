from serial import Serial

from CollisionStatusGenerator import CollisionStatusGenerator
from Response import Response
from ResultStatus import ResultStatus


class Receiver:
    def __init__(self, port_name: str, collision_appearance_probability: int = 0):
        self.__port_name = port_name
        self.__port = Serial(port_name, 9600)
        self.__collision_status_generator = CollisionStatusGenerator(collision_appearance_probability)

    def receive_byte(self) -> Response:
        byte = ''
        if self.__port.inWaiting() > 0:
            byte = self.__port.read().decode('cp1251')
        if self.__collision_status_generator.is_collision_occurred():
            return Response(ResultStatus.ERROR)
        return Response(ResultStatus.OK, data=byte)
