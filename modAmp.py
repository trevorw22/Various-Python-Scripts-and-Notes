# Waveform plotting script using matplotlib

import matplotlib.pyplot as plot
import numpy as np
from scipy import signal

t = np.arange(0.0, 2, 0.01)
freq = 10
freqs = 1
m = 0.9 #by increasing this value we can increase the carrier signal or amplitude
y = (1 + m * np.sin(2 * np.pi * freqs * t))* np.sin(2 * np.pi * freq * t)
plot.xlabel('time')
plot.ylabel('amplitude')
plot.plot(t,y)
plot.show()
