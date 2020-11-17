import numpy as np
import sounddevice as sd
import serial 
import time

ser = serial.Serial('COM7',500000) #dependent on computer / arduino / USB port
time.sleep(3) #allow time for Arduino / Serial to initialize
ser.write((str(5) + 'd').encode()) #d is endmarker
duration = 1000 #in seconds
sd.default.samplerate = 44100

#Choose INPUT device (Usually Stereo Mix / Microphone) 
print(sd.query_devices())
x = int(input("Choose device "))
sd.default.device = x

#Calculate Audio
volume_norm = 0
def audio_callback(indata, frames, time, status):
   volume_norm = np.linalg.norm(indata) * 10
   print(str(int(volume_norm)) + '\n')
   print("|" * int(volume_norm))
   ser.write((str(int(volume_norm) * 3) +'d').encode())

#continuously run
stream = sd.InputStream(callback=audio_callback)
with stream:
   while True:
      sd.sleep(duration * 10000) 
   
 