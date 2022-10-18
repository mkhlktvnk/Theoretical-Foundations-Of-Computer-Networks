import collections
from tkinter import *
from serial import *

from accessify import private

from ErrorGenerator import ErrorGenerator
from PackagesProcessorUtils import PackagesProcessorUtils


class Application:
    def __init__(self):
        self.__root = Tk()
        self.__root.title('COM-PORT')
        self.__root.geometry('1400x350')
        # init text field
        self.__user_input = Text(self.__root)
        self.__packages_output = Text(self.__root)
        self.__result_output = Text(self.__root)
        self.__log_output = Text(self.__root)
        # init labels
        self.__user_input_label = Label(self.__root, text='Input')
        self.__packages_output_label = Label(self.__root, text='Package')
        self.__result_output_label = Label(self.__root, text='Result')
        self.__log_label = Label(self.__root, text='Log')
        # init buttons
        self.__send_button = Button(text='Send')
        self.__clear_button = Button(text='Clear')
        # bind buttons and text fields
        self.__send_button.bind('<Button-1>', self.send_button_onclick)
        self.__clear_button.bind('<Button-1>', self.clear_button_onclick)
        # place text fields
        self.place_text_fields(350, 250)
        # place labels
        self.place_labels(250, 50)
        # place buttons
        self.place_buttons(50, 20)
        # configure text fields
        self.disable_text_field(self.__result_output)
        self.disable_text_field(self.__packages_output)
        self.disable_text_field(self.__result_output)
        self.disable_text_field(self.__log_output)
        # init spinbox
        self.__spinbox_var = StringVar(value='0')
        self.__spinbox = Spinbox(from_=0, to=24, textvariable=self.__spinbox_var, state='readonly')
        self.__spinbox.place(width=100, height=25, x=200, y=10)
        # init ports
        self.__port1 = Serial()
        self.__port2 = Serial()
        try:
            self.__port1 = Serial('COM1', 9600)
            self.__port2 = Serial('COM2', 9600)
        except SerialException:
            self.make_log('Cant open ports!')

    def start(self) -> None:
        self.__root.mainloop()

    def send_button_onclick(self, event):
        if not self.__port1.isOpen() or not self.__port2.isOpen():
            return
        data = self.get_user_input()
        packages = self.split_packages(data)
        packages = self.clear_packages(packages)
        debug_list = PackagesProcessorUtils.validate_packages(packages)
        if len(debug_list) != 0:
            self.make_list_log(debug_list)
            return
        checksums = PackagesProcessorUtils.generate_checksums(packages)
        packages = PackagesProcessorUtils.append_checksum_to_packages(packages, checksums)
        self.clear_text_field(self.__log_output)
        self.make_log('Sent checksums:')
        self.make_list_log(checksums)
        try:
            corrupted = int(self.__spinbox.get())
        except ValueError:
            self.make_log('Nums of corrupted is not integer')
            return
        error_generator = ErrorGenerator(corrupted, packages)
        packages = error_generator.generate_errors()
        print(packages)
        self.clear_text_field(self.__packages_output)
        self.show_packages(packages)
        self.send_packages(packages)
        received = []
        for package in packages:
            self.__port2.write(package.encode('cp1251'))
            received.append(self.__port2.read(len(package)).decode('cp1251'))
        separated = PackagesProcessorUtils.separate_packages(received)
        received_data = separated[0]
        received_checksums = PackagesProcessorUtils.generate_checksums(received_data)
        self.make_log('Receiver checksums:')
        self.make_list_log(received_checksums)
        self.clear_text_field(self.__result_output)
        self.show_received_data(received_data)
        if collections.Counter(received_checksums) != collections.Counter(checksums):
            self.make_log('Error! Sender and receiver checksums are not equal!')
            return

    def clear_button_onclick(self, event):
        self.__user_input.delete(1.0, END)
        self.clear_text_field(self.__result_output)
        self.clear_text_field(self.__packages_output)
        self.clear_text_field(self.__log_output)

    @private
    def split_packages(self, data: str) -> list:
        return data.split('\n')

    @private
    def clear_packages(self, packages: list) -> list:
        stripped = []
        for i in range(len(packages) - 1):
            packages[i] = packages[i].strip()
            stripped.append(packages[i].replace('\b', ''))
        return stripped

    @private
    def send_packages(self, packages: list):
        for package in packages:
            self.__port1.write(package.encode('cp1251'))

    @private
    def receive_packages(self) -> list:
        received = []
        while self.__port2.inWaiting() > 0:
            out = self.__port2.read(self.__port1.inWaiting()).decode('cp1251')
            received.append(out)
        return received

    @private
    def receive_package(self) -> str:
        out = ''
        while self.__port2.inWaiting() > 0:
            item = self.__port2.read().decode('cp1251')
            print(item)
            out += item
        return out

    @private
    def place_text_fields(self, width: int, height: int) -> None:
        self.__user_input.place(width=width, height=height, x=0, y=50)
        self.__packages_output.place(width=width, height=height, x=350, y=50)
        self.__result_output.place(width=width, height=height, x=700, y=50)
        self.__log_output.place(width=width, height=height, x=1050, y=50)

    @private
    def place_labels(self, width: int, height: int) -> None:
        self.__user_input_label.place(width=width, height=height, x=0)
        self.__packages_output_label.place(width=width, height=height, x=350)
        self.__result_output_label.place(width=width, height=height, x=700)
        self.__log_label.place(width=width, height=height, x=1050)

    @private
    def place_buttons(self, width: int, height: int) -> None:
        self.__send_button.place(width=width, height=height, x=350, y=315)
        self.__clear_button.place(width=width, height=height, x=400, y=315)

    @private
    def disable_text_field(self, text_field: Text) -> None:
        text_field.config(state='disabled')

    @private
    def enable_text_field(self, text_field: Text) -> None:
        text_field.config(state='normal')

    @private
    def get_user_input(self):
        return self.__user_input.get(1.0, END)

    @private
    def clear_text_field(self, text_field: Text):
        self.enable_text_field(text_field)
        text_field.delete(1.0, END)
        self.disable_text_field(text_field)

    @private
    def make_log(self, data: str):
        self.enable_text_field(self.__log_output)
        self.__log_output.insert(END, data + '\n')
        self.disable_text_field(self.__log_output)

    @private
    def make_list_log(self, data: list):
        self.enable_text_field(self.__log_output)
        for item in data:
            self.__log_output.insert(END, item + '\n')
        self.disable_text_field(self.__log_output)

    @private
    def show_received_data(self, data: list):
        self.enable_text_field(self.__result_output)
        for item in data:
            self.__result_output.insert(END, item + '\n')
        self.disable_text_field(self.__result_output)

    @private
    def show_packages(self, staffed: list):
        self.enable_text_field(self.__packages_output)
        for item in staffed:
            self.__packages_output.insert(END, item + '\n\n')
        self.disable_text_field(self.__packages_output)
