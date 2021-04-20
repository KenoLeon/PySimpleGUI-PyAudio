import pyaudio
import numpy as np

"""Simple Blocking Stream PyAudio"""

CHUNK = 1024  # Samples: 1024,  512, 256, 128
RATE = 44100  # Equivalent to Human Hearing at around 40 kHz
INTERVAL = 5  # Sampling Interval in Seconds

# If you are having trouble  making sense of the above, this might help:
# CHUNK: How many slices of sound
# RATE: How Fast these slices are captured
# INTERVAL: How much time to listen


# INIT PyAudio Instance
p = pyaudio.PyAudio()

# OPEN/Configure Stream:
stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

# Loop Continuously:
while True:
    for i in range(int(INTERVAL*RATE/CHUNK)):  # STREAN INTERVAL
        data = np.fromstring(stream.read(CHUNK), dtype=np.int16)
        print(np.amax(data))
        print(data.shape)

# Exit with ctrl+C"
# This never runs.

stream.stop_stream()
stream.close()
p.terminate()
