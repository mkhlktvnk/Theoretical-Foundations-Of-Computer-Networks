import random

from ChannelStatus import ChannelStatus


class ChanelAccessGenerator:
    def __init__(self, availability_percentage: int):
        self.__availability_percentage = availability_percentage

    def set_availability_percentage(self, availability_percentage: int):
        self.__availability_percentage = availability_percentage

    def generate_channel_access(self):
        weights = [self.__availability_percentage / 100, 1 - (self.__availability_percentage / 100)]
        return random.choices([ChannelStatus.FREE, ChannelStatus.BUSY], weights)[0]
