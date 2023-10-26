import serial
import numpy as np
import matplotlib as plt

# Close any existing open serial ports
if serial.Serial:
    serial.Serial().close()

# Open the serial port
s = serial.Serial("COM3", baudrate=57600)

def FeatureExtract(y):
    # y trong truong hop nay co do dai 15*512
    flm = 512
    L = len(y)
    Y = np.fft.fft(y)
    Y[0] = 0
    P2 = np.abs(Y / L)
    P1 = P2[:L // 2 + 1]
    P1[1:-1] = 2 * P1[1:-1] #hàm chứa giá tr của fft
    plt.plot(P1)
    plt.show()

    # Find the indices of the frequency values between 0.5 Hz and 4 Hz
    f1 = np.arange(len(P1)) * flm / len(P1) # co thằng x lại
    indices1 = np.where((f1 >= 0.5) & (f1 <= 4))[0]
    delta = np.sum(P1[indices1])

    f1 = np.arange(len(P1)) * flm / len(P1)
    indices1 = np.where((f1 >= 4) & (f1 <= 8))[0]
    theta = np.sum(P1[indices1])

    f1 = np.arange(len(P1)) * flm / len(P1)
    indices1 = np.where((f1 >= 8) & (f1 <= 13))[0]
    alpha = np.sum(P1[indices1])

    f1 = np.arange(len(P1)) * flm / len(P1)
    indices1 = np.where((f1 >= 13) & (f1 <= 30))[0]
    beta = np.sum(P1[indices1])

    abr = alpha / beta
    tbr = theta / beta
    dbr = delta / beta
    tar = theta / alpha
    dar = delta / alpha
    dtabr = (alpha + beta) / (delta + theta)
    dict = {"delta": delta,
            "theta": theta,
            "alpha": alpha,
            "beta": beta,
            "abr": abr,
            "tbr": tbr,
            "dbr": dbr,
            "tar": tar,
            "dar": dar,
            "dtabr": dtabr
            }
    #print(dict)
    return dict


filename = ''
x = 0
y = []
z = []
feature = []
feature_names = ['delta', 'theta', 'alpha', 'beta', 'abr', 'tbr', 'dbr', 'tar', 'dar', 'dtabr']
sliding_window_start = 0
sliding_window_end = 0
k = 15 * 512
print("START!")
while x < (3600 * 512):
    noise = 0
    x += 1
    data = s.readline().decode('utf-8').rstrip("\r\n")  # strip removes leading/trailing whitespace
    if data:
        value = int(float(data))
    else:
        x -= 1
        continue
    print(value)
    y.append(value)

# Use to get data
# df = pd.DataFrame.from_dict(feature)
# df.to_csv("Banmoi.csv")

# Close the serial port
print("DONE")
s.close()