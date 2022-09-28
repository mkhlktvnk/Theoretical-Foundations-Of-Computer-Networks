

from BitStaffingProcessor import BitStaffingProcessor
from CheckSumGenerator import CheckSumGenerator
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
        checksums_list = []
        for package in packages:
            checksums_list.append(CheckSumGenerator(package).generate())
        return checksums_list

    @staticmethod
    def perform_packages_bit_staffing(packages: list) -> list:
        staffed_list = []
        for package in packages:
            staffed_list.append(BitStaffingProcessor(package).perform_bit_staffing())
        return staffed_list

    @staticmethod
    def perform_packages_bit_destaffing(packages: list) -> list:
        destaffed_list = []
        for package in packages:
            destaffed_list.append(BitStaffingProcessor(package).perform_bit_destaffing())
        return destaffed_list

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
