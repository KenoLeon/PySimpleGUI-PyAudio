import pyaudio
import time
import numpy as np

"""Simple Non Blocking Stream PyAudio"""

CHUNK = 1024  # Samples: 1024,  512, 256, 128 frames per buffer
RATE = 44100  # Equivalent to Human Hearing at 40 kHz
INTERVAL = 1  # Sampling Interval in Seconds


p = pyaudio.PyAudio()

# This callback gets called by the stream


def callback(in_data, frame_count, time_info, status):
    # print(in_data)
    data = np.fromstring(in_data, dtype=np.int16)
    print(np.amax(data))
    return (in_data, pyaudio.paContinue)


# Notice the extra stream callback...
stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK,
                stream_callback=callback)

stream.start_stream()

# The loop is different as well...
while stream.is_active():
    time.sleep(0.1)

# Exit with ctrl+C"
# This still doesn't run.

stream.stop_stream()
stream.close()
p.terminate()
