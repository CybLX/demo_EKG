import numpy as np
import matplotlib.pyplot as plt
import pywt

data = np.loadtxt('./einthoven32.txt').T
tempo, ecg = data[0],data[1]
#ecg = pywt.data.ecg()[0:2000]
coeffs = pywt.swt(ecg, wavelet='sym4',level=3, trim_approx=True, norm=True)
ca = coeffs[0]
details = coeffs[1:]

print("Variance of the ecg signal = {}".format(np.var(ecg, ddof=1)))
variances = [np.var(c, ddof=1) for c in coeffs]
detail_variances = variances[1:]

print("Sum of variance across all SWT coefficients = {}".format(np.sum(variances)))
ylim = [ecg.min(), ecg.max()]
plt.plot(ecg)
plt.legend(['Original signal'])

fig, axes = plt.subplots(len(coeffs))
axes[0].set_title("normalized SWT decomposition")
axes[0].plot(ecg)
axes[0].set_ylabel('ECG Signal')
axes[0].set_xlim(0, len(ecg) - 1)
axes[0].set_ylim(ylim[0], ylim[1])

for i, x in enumerate(coeffs):
    ax = axes[-i - 1]
    ax.plot(coeffs[i], 'g')
    if i == 0:
        ax.set_ylabel("A%d" % (len(coeffs) - 1))
    else:
        ax.set_ylabel("D%d" % (len(coeffs) - i))
    # Scale axes
    ax.set_xlim(0, len(ecg) - 1)
    ax.set_ylim(ylim[0], ylim[1])

# reorder from first to last level of coefficients
level = np.arange(1, len(detail_variances) + 1)

# create a plot of the variance as a function of level
plt.figure(figsize=(8, 6))
fontdict = dict(fontsize=16, fontweight='bold')
plt.plot(level, detail_variances[::-1], 'k.')
plt.xlabel("Decomposition level", fontdict=fontdict)
plt.ylabel("Variance", fontdict=fontdict)
plt.title("Variances of detail coefficients", fontdict=fontdict)
plt.show()

