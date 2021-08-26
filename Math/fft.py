import numpy as np
import matplotlib.pyplot as plot

# Construct the time signal

fs = 2000  # sampling frequency
tstep = 1/fs  # sample time interval
f0 = 100  # signal frequency
n = int(25*fs/f0)  # number of samples

t = np.linspace(0, (n-1)*tstep, n)  # time steps
fstep = fs/n
f = np.linspace(0, (n-1)*fstep, n)  # frequency steps
y = 1 * np.sin(2 * np.pi * f0 * t)

# Perform the Fast Fourier Transform
x = np.fft.fft(y)
xMag = np.abs(x)/n  # normalize

fPlot = f[0:int(n/2+1)]
xMagPlot = 2 * xMag[0:int(n/2+1)]
xMagPlot[0] = xMagPlot[0]/2  # DC component does not need to multiply by 2

# Plot the time signal and frequency spectrum
fig, [ax1, ax2] = plot.subplots(nrows=2, ncols=1)
ax1.plot(t, y, '.-')
ax2.plot(fPlot, xMagPlot, '.-')
plot.show()
