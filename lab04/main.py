import random

from Receiver import Receiver
from Response import Response
from ResultStatus import ResultStatus
from Transmitter import Transmitter


def calculate_results(results: list[Response]) -> list[int]:
    successful = 0
    failed = 0
    for result in results:
        if result.get_status() == ResultStatus.OK:
            successful += 1
        else:
            failed += 1
    return [successful, failed]


if __name__ == '__main__':
    collision = 50
    free_channel = 50
    data = "a"
    transmitter = Transmitter("COM1", free_channel_probability=free_channel,
                              collision_appearance_probability=collision)
    receiver = Receiver("COM2", collision)
    transmitter_responses = []
    receiver_responses = []
    for i in range(10):
        random.seed(random.randint(-1000000, 1000000))
        transmitter_response = transmitter.send_package('a')
        receiver_response = receiver.receive_byte()
        transmitter_responses.append(transmitter_response)
        receiver_responses.append(receiver_response)
        print('--------------------------------------------------')
        print('transmitter status = ' + str(transmitter_response.get_status()))
        print('receiver status = ' + str(receiver_response.get_status()))
        print('received data = ' + str(receiver_response.get_data()))
    print('--------------------------------------------------')
    transmitter_results = calculate_results(transmitter_responses)
    receiver_results = calculate_results(receiver_responses)
    print('Transmitter: ')
    print('successful: ' + str(transmitter_results[0]) + ', failed: ' + str(transmitter_results[1]))
    print('Receiver: ')
    print('successful: ' + str(receiver_results[0]) + ', failed: ' + str(receiver_results[1]))
