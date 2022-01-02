import random
file=open("random.txt","a")
tl=[]
tt=0
for i in range(10000000):
    _=file.write(str(random.random())+",")
    
file.close()
print("Done!")



