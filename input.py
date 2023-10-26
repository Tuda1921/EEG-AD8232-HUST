import serial
import time
import matplotlib.pyplot as plt
import numpy as np

# Close any existing open serial ports
if serial.Serial:
    serial.Serial().close()

# Open the serial port
s = serial.Serial("COM3", baudrate=57600)
x = 0
y = []
start_time = time.time()
end_time = time.time()
while end_time - start_time <= 5:
    x = x + 1
    data = s.readline()  # strip removes leading/trailing whitespace
    try:
        value = data.decode().split('\r\n')[0]
        y.append(int(float(value)))
    except ValueError:
        pass
    end_time = time.time()
print(x)
print(y)
print(len(y))

flm = len(y)/5
L = len(y)
Y = np.fft.fft(y)
Y[0] = 0
P2 = np.abs(Y / L)
P1 = P2[:L // 2 + 1]
P1[1:-1] = 2 * P1[1:-1]  # hàm chứa giá tr của fft
plt.plot(P1)
plt.show()

s.close()
