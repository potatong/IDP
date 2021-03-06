import glob
import serial
import struct
import time

def find_usb_port():
    #gets list of ports
    ports = glob.glob('/dev/tty.*')

    #finds usb port
    for port_test in ports:
        if 'usb' in port_test:
            return port_test
    
    return 0

def establish_serial(port):
    #create serial connection to board
    try:
        board = serial.Serial(port,9600)
    #raise error if no usb port is found
    except ValueError:
        print('ValueError: No USB port found')
        return 0
    except OSError:
        print('OSError: Couldn\'t connect to port')
        return 0
    return board

def read_next_line(board,decode=False,strip=True):
    #read serial output from board
    try:
        line = board.readline()
        if not decode:
            return(line)
        else:
            if not strip:
                return(line.decode())
            else:
                return(line.decode().rstrip('\r\n'))
    except:
        print('Failed')
       # print('Error: Couldn\'t read line from serial')

def write_serial(msg,board):
    print(msg)
    #msg2 = struct.pack('>B',msg)
    #print(msg2)
    try:
        board.write(msg)
        #board.write(msg2)
    except:
        print('Error: Couldn\'t write line to serial')

board = establish_serial(find_usb_port())

wait = 2
'''
while True:
    write_serial(b'\x01',board)
    time.sleep(wait)
    while board.inWaiting() > 0:
        line = read_next_line(board,decode=True,strip=True)
        if line != 255:
            print(line)
    write_serial(b'\x02',board)
    time.sleep(wait)
    while board.inWaiting() > 0:
        line = read_next_line(board,decode=True,strip=True)
        if line != 255:
            print(line)
'''

while True:
    while board.inWaiting() > 0:
        line = read_next_line(board,decode=True,strip=True)
        print(line)

