#!usr/bin/env python  
#coding=utf-8 
 
import pyaudio
import thread
import wave
import sys

chunk = 1024

def play(audio):
	thread.start_new_thread(th,(audio,))

def th(audio):
	wf = wave.open(audio + ".wav", "rb")
	p = pyaudio.PyAudio()
	stream = p.open(format =
		p.get_format_from_width(wf.getsampwidth()),
		channels = wf.getnchannels(),
		rate = wf.getframerate(),
		output = True)
	data = wf.readframes(chunk)
	while data != '':
		stream.write(data)
		data = wf.readframes(chunk)
	stream.close()
	p.terminate()
