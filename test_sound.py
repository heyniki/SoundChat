import math
import numpy
import pyaudio

CHUNK = 1024
FORMAT = pyaudio.paFloat32
CHANNELS = 1
RATE = 46080

def sine_wave(frequency, framerate, amplitude,secs):
    period = int(framerate / frequency)
#    if amplitude > 1.0: amplitude = 1.0
    if amplitude < 0.0: amplitude = 0.0
    lookup_table = [float(amplitude) * math.sin(2.0*math.pi*float(frequency)*(float(i%period)/float(framerate))) for i in xrange(period)]
    return numpy.array([lookup_table[i%period] for i in xrange(framerate)]*secs)

def generate_sound(freq, amp, samp_rate, secs):
  p = pyaudio.PyAudio()

  stream = p.open(format=FORMAT,
          channels=CHANNELS,
          rate=RATE,
          output=True,
          frames_per_buffer=CHUNK)

  stream.write(sine_wave(freq, samp_rate, amp, secs))

  stream.stop_stream()

  stream.close()
  p.terminate()

generate_sound(23000, 10, 44100, 2)
