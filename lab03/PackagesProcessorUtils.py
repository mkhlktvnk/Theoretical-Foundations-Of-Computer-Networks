from CRCProcessor import CRCProcessor
from InvalidPackageException import InvalidPackageException
from PackageValidator import PackageValidator


class PackagesProcessorUtils:
    @staticmethod
    def validate_packages(packages: list) -> list:
        debug_list = []
        for package in packages:
            try:
                PackageValidator(package, 32).validate()
            except InvalidPackageException as e:
                debug_list.append(e.get_message())
        return debug_list

    @staticmethod
    def generate_checksums(packages: list) -> list:
        crc_processor = CRCProcessor()
        checksums = []
        for package in packages:
            checksums.append(crc_processor.crc_16(package))
        return checksums

    @staticmethod
    def convert_packages_to_bin(packages: list) -> list:
        converted = []
        for package in packages:
            converted.append(str(bin(int(package, 16)))[2:34])
        return converted

    @staticmethod
    def convert_packages_to_hex(packages: list) -> list:
        converted = []
        for package in packages:
            converted.append(str(hex(int(package, 2)))[2:34])
        return converted

    @staticmethod
    def append_checksum_to_packages(packages: list, checksums: list) -> list:
        appended = []
        length = len(checksums)
        for i in range(length):
            appended.append(packages[i] + checksums[i])
        return appended

    @staticmethod
    def separate_packages(packages: list) -> list:
        checksums = []
        data = []
        for package in packages:
            data.append(package[0:32])
            checksums.append(package[32:])
        return [data, checksums]


