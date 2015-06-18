#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 jaidev <jaidev@newton>
#
# Distributed under terms of the MIT license.

"""
Example from section 3.1.4 of the tutorial.
"""

import numpy as np
from tftb.processing.linear import stft
from tftb.generators import fmlin, amgauss
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

x = np.real(amgauss(128) * fmlin(128)[0])
window = np.ones((128,))
tfr, _, _ = stft(x, n_fbins=128, window=window)
threshold = np.abs(tfr) * 0.05
tfr[np.abs(tfr) <= threshold] = 0.0 * 1j * 0.0

fig, axImage = plt.subplots(figsize=(10, 8))
axImage.imshow(np.abs(tfr[:64, :]) ** 2, cmap=plt.cm.gray, origin='bottomleft',
               extent=[0, 128, 0, 0.5], aspect='auto')
axImage.grid(True)
axImage.set_title("STFT squared modulus")
axImage.set_ylabel('Frequency')
axImage.set_xlabel('Time')
axImage.yaxis.set_label_position("right")

divider = make_axes_locatable(axImage)
axTime = divider.append_axes("top", 1.2, pad=0.5)
axFreq = divider.append_axes("left", 1.2, pad=0.5)
axTime.plot(np.real(x))
axTime.set_xticklabels([])
axTime.set_xlim(0, 128)
axTime.set_ylabel('Real part')
axTime.set_title('Signal in time')
axTime.grid(True)
axFreq.plot((abs(np.fft.fftshift(np.fft.fft(x))) ** 2)[::-1][:64],
            np.arange(x.shape[0] / 2))
axFreq.set_ylim(0, x.shape[0] / 2 - 1)
axFreq.set_ylabel('Spectrum')
axFreq.set_yticklabels([])
axFreq.set_xticklabels([])
axFreq.grid(True)
axFreq.invert_xaxis()
plt.show()
