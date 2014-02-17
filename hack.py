"""PyAudio example: Record a few seconds of audio and save to a WAVE file."""

import pyaudio
import numpy
import scipy
import matplotlib.pyplot as plt
import math

CHUNK = 1024
FORMAT = pyaudio.paFloat32
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 3

def listen():

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
          channels=CHANNELS,
          rate=RATE,
          input=True,
          frames_per_buffer=CHUNK)

    print("* recording")

    frames = []

    for i in xrange(0, int(RATE / CHUNK * RECORD_SECONDS)):
      data = stream.read(CHUNK)
      frames.append(data)

    data = ''.join(frames)
    print("* done recording")

    stream.stop_stream()

    stream.close()
    p.terminate()

    data = numpy.fromstring(data, 'Float32')

    f_signal = numpy.fft.fft(data)
    W = numpy.fft.fftfreq(data.size, 1.0/RATE)
    cut_f_signal = f_signal.copy()
    cut_f_signal[(W<22000)] = 0
    cut_signal = numpy.fft.ifft(cut_f_signal)
    plt.plot(numpy.arange(cut_signal.size), cut_signal)
    plt.show()

listen()
