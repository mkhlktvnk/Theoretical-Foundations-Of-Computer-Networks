class PackageParser:
    def __init__(self, package: str):
        self.__package = package

    def parse_flag(self) -> str:
        return self.__package[0:2]

    def parse_data_length(self) -> str:
        return self.__package[2:4]

    def parse_source_address(self) -> str:
        return self.__package[4:6]

    def parse_destination_address(self) -> str:
        return self.__package[6:8]

    def parse_data(self) -> str:
        return self.__package[8:34]
