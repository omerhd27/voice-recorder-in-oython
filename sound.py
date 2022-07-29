from numpy import record
import sounddevice
from scipy.io.wavfile import write

fs=44100

second=int(input("enter the recording time: "))
print("recording....\n")
record_voice=sounddevice.rec(int(second * fs),samplerate=fs,channels=2)
sounddevice.wait()
write("MyRecording.wav",fs,record_voice)
print("recording is done please check it")