import unittest

from ChanelStatusGenerator import ChanelAccessGenerator
from ChannelStatus import ChannelStatus


class TestChannelStatusGenerator(unittest.TestCase):
    def setUp(self) -> None:
        self.__channel_access_generator = ChanelAccessGenerator(0)

    def test_free_access(self):
        self.__channel_access_generator.set_availability_percentage(100)
        self.assertEqual(self.__channel_access_generator.generate_channel_access(), ChannelStatus.FREE)

    def test_busy_access(self):
        self.__channel_access_generator.set_availability_percentage(0)
        self.assertEqual(self.__channel_access_generator.generate_channel_access(), ChannelStatus.BUSY)


if __name__ == "__main__":
    unittest.main()
