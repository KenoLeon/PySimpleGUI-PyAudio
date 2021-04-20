import PySimpleGUI as sg
import pyaudio
import numpy as np

"""PyAudio PySimpleGUI  Non Blocking Stream for Microphone"""

# VARS CONSTS:
# Added a stream reference

_VARS = {'window': False,
         'stream': False}

# pysimpleGUI INIT:
# New Stop Button :
AppFont = 'Any 16'
sg.theme('DarkTeal2')
layout = [[sg.ProgressBar(10000, orientation='h',
                          size=(20, 20), key='-PROG-')],
          [sg.Button('Listen', font=AppFont),
           sg.Button('Stop', font=AppFont),
           sg.Button('Exit', font=AppFont)]]
_VARS['window'] = sg.Window('Mic Max Data', layout, finalize=True)


# PyAudio INIT:
CHUNK = 1024  # Samples: 1024,  512, 256, 128
RATE = 44100  # Equivalent to Human Hearing at 40 kHz
INTERVAL = 1  # Sampling Interval in Seconds ie Interval to listen

# Global Pyaudio Instance:
pAud = pyaudio.PyAudio()


def stop():
    # New Stop Method where we stop & close the stream"
    if _VARS['stream']:
        _VARS['stream'].stop_stream()
        _VARS['stream'].close()
        _VARS['window']['-PROG-'].update(0)


def callback(in_data, frame_count, time_info, status):
    # print(in_data)
    data = np.frombuffer(in_data, dtype=np.int16)
    # print(np.amax(data))
    _VARS['window']['-PROG-'].update(np.amax(data))
    return (in_data, pyaudio.paContinue)


def listen():
    _VARS['stream'] = pAud.open(format=pyaudio.paInt16,
                                channels=1,
                                rate=RATE,
                                input=True,
                                frames_per_buffer=CHUNK,
                                stream_callback=callback)

    _VARS['stream'].start_stream()


while True:
    event, values = _VARS['window'].read(timeout=100)
    if event == sg.WIN_CLOSED or event == 'Exit':
        pAud.terminate()
        break
    if event == 'Listen':
        listen()
    if event == 'Stop':
        stop()

_VARS['window'].close()
