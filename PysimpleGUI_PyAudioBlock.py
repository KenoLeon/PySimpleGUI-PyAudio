import PySimpleGUI as sg
import pyaudio
import numpy as np


# VARS CONSTS:
_VARS = {'window': False}

# pysimpleGUI INIT:
AppFont = 'Any 16'
sg.theme('DarkTeal3')
layout = [[sg.ProgressBar(10000, orientation='h',
                          size=(20, 20), key='-PROG-')],
          [sg.Button('Listen', font=AppFont),
           sg.Button('Exit', font=AppFont)]]
_VARS['window'] = sg.Window('Mic Max Data', layout, finalize=True)


# PyAudio INIT:
CHUNK = 1024  # Samples: 1024,  512, 256, 128
RATE = 44100  # Equivalent to Human Hearing at 40 kHz
INTERVAL = 4  # Sampling Interval in Seconds ie Interval to listen


def listen():
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
    for i in range(int(INTERVAL*RATE/CHUNK)):
        data = np.frombuffer(stream.read(CHUNK), dtype=np.int16)
        chunkMax = np.amax(data)
        print(chunkMax)
        _VARS['window']['-PROG-'].update(chunkMax)
    _VARS['window']['-PROG-'].update(0)
    stream.stop_stream()
    stream.close()
    p.terminate()


while True:
    event, values = _VARS['window'].read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Listen':
        listen()

_VARS['window'].close()
