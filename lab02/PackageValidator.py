from accessify import private

from InvalidPackageException import InvalidPackageException
from PackageParser import PackageParser


class PackageValidator:
    def __init__(self, package: str, required_package_length: int):
        self.__package = package
        self.__package_parser = PackageParser(package)
        self.__required_package_length = required_package_length

    def validate(self):
        try:
            hex(int(self.__package[0:self.__required_package_length], 16))
        except ValueError:
            raise InvalidPackageException('Package is not hexadecimal!')
        if not self.package_length_valid():
            raise InvalidPackageException('Package length is not valid!')
        if not self.package_flag_valid():
            raise InvalidPackageException('Package flag is not valid! 7e required.')
        if not self.package_length_field_valid():
            raise InvalidPackageException('Package length field is not valid! 0c required.')

    @private
    def package_length_valid(self):
        return len(self.__package) == self.__required_package_length

    @private
    def package_flag_valid(self):
        return self.__package_parser.parse_flag() == '7e'

    @private
    def package_length_field_valid(self):
        return self.__package_parser.parse_data_length() == '0c'
