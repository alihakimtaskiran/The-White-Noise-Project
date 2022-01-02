import numpy as np
from scipy.io.wavfile import write
with open("random.txt") as file:
    s=[]
    sv=file.read().split(",")
    print(len(sv))
    for i in sv[:-1]:
        s.append(float(i))
    file.close()

print(len(s))
write("white-noise.wav",5000000,np.array(s))
print("Done!")
