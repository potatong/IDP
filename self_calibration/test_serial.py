from serial_con import *

port = find_usb_port()

assert type(port != 'int')

assert establish_serial(port) == 1

print(read_serial())