from tkinter import *
import serial
import serial.tools.list_ports


class MainWindow:
    def __init__(self):
        self.main_window = Tk()
        self.main_window.title('COM-PORT')
        self.main_window.geometry('600x300')
        self.input = Text(self.main_window)
        self.output = Text(self.main_window)
        self.log = Text(self.main_window)
        self.input.place(width=200, height=250, x=0)
        self.output.place(width=200, height=250, x=200)
        self.output.config(state='disabled')
        self.log.place(width=200, height=250, x=400)
        self.log.config(state='disabled')
        self.log.insert('1.0', 'Port is open')
        self.input_label = Label(self.main_window, text="Input to port")
        self.output_label = Label(self.main_window, text="Output from port")
        self.log_label = Label(self.main_window, text="Log")
        self.input_label.place(width=200, height=50, x=0, y=250)
        self.output_label.place(width=200, height=50, x=200, y=250)
        self.log_label.place(width=200, height=50, x=400, y=250)
        self.input.bind("<Key>", self.on_input_update)
        self.port1 = serial.Serial
        self.port2 = serial.Serial
        self.open_ports()

    def open_ports(self):
        try:
            self.port1 = serial.Serial('COM1', 9600)
            self.port2 = serial.Serial('COM2', 9600)
            self.make_log('Ports is open. Now you can send data')
        except serial.SerialException:
            self.make_log('Error opening ports')

    def on_input_update(self, event):
        if len(list(serial.tools.list_ports.comports())) == 0:
            self.open_ports()
        self.output.config(state='normal')
        self.send_data(event.char.encode('cp1251'))
        out = self.read_data()
        if out == '\b':
            self.output.delete('end-2c')
            return
        self.output.insert(END, out)
        self.output.config(state='disabled')

    def send_data(self, data):
        try:
            self.port1.write(data)
        except serial.PortNotOpenError:
            self.make_log('Ports are closed')

    def read_data(self):
        out = ''
        while self.port2.inWaiting() > 0:
            try:
                out = self.port2.read(1).decode('cp1251')
            except serial.PortNotOpenError:
                self.make_log('Ports are closed')
        return out

    def make_log(self, message):
        self.log.config(state='normal')
        self.log.delete('1.0', END)
        self.log.insert('1.0', message)

        self.log.config(state='disabled')


if __name__ == "__main__":
    app = MainWindow()
    app.main_window.mainloop()
