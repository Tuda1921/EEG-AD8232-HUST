import serial
import time
import matplotlib.pyplot as plt
import numpy as np

# Close any existing open serial ports
if serial.Serial:
    serial.Serial().close()

# Open the serial port
s = serial.Serial("COM3", baudrate=57600)

# wait 1 second
start_time = time.time()
end_time = time.time()
while end_time - start_time <= 1:
    data = s.readline()  # strip removes leading/trailing whitespace
    end_time = time.time()

# start
N = 10
x = 0
y = []
start_time = time.time()
end_time = time.time()
while end_time - start_time <= N:
    x = x + 1
    data = s.readline()  # strip removes leading/trailing whitespace
    try:
        value = data.decode().split('\r\n')[0]
        y.append(int(float(value)))
    except ValueError:
        pass
    end_time = time.time()
print(x)
print(len(y))
print(len(y) / N)
print(y)

# Slidingwindow


# FFT
flm = len(y) / N
L = len(y)
Y = np.fft.fft(y)
Y[0] = 0
P2 = np.abs(Y / L)
P1 = P2[:L // 2 + 1]
P1[1:-1] = 2 * P1[1:-1]  # hàm chứa giá tr của fft
f1 = np.arange(len(P1)) * flm / len(P1) / 2  # scale x
plt.plot(f1, P1)

plt.show()

s.close()
