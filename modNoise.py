# Waveform plotting script using matplotlib with noise

import matplotlib.pyplot as plot
import numpy as np
from scipy import signal

xs = np.arange(0.0, 2, 0.01)
ys = signal.sawtooth(2 * np.pi * 5 * xs)
noise = 0.1*np.random.normal(0, 1, len(xs))
ys = ys + noise
plot.xlabel('time')
plot.ylabel('amplitude')
plot.plot(xs,ys)
plot.show()
