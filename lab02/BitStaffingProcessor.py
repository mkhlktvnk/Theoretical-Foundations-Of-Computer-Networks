class BitStaffingProcessor:
    def __init__(self, package: str):
        self.__BYTE_PATTERN = '0111111'
        self.__BIT_STAFFING = '1'
        self.__package = package

    def perform_bit_staffing(self) -> str:
        out = ''
        for i in range(0, len(self.__package), 2):
            out += str(bin(int(self.__package[i:i + 2], 16)))[2:].rjust(8, '0')
        out = out[0:8] + out[8:].replace(self.__BYTE_PATTERN, self.__BYTE_PATTERN + self.__BIT_STAFFING)
        return out

    def perform_bit_destaffing(self) -> str:
        out = self.__package[0:8] + self.__package[8:].replace(self.__BYTE_PATTERN + self.__BYTE_PATTERN,
                                                               self.__BYTE_PATTERN)
        return out
