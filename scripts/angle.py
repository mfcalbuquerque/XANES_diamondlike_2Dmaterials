import matplotlib.pyplot as plt
import sys
import numpy as np

f=open("angle-dependence.dat", "a")
f.write("##   sin2('\u03B1')   peak intensity (arb. uni.)")
ang=[0.0, 0.35, 0.79, 1.05, 1.31, 1.57]

sin_ang=np.square(np.sin(ang))
sss=list(sin_ang)
maximum=[]
#pre_max=[]

a=float(3.3)
b=float(5.6)
col=[]

blabla=open("xanes_x.dat","r")
jjj=blabla.readlines()[4:]

for lll in jjj:
    nnn=lll.split()
    col.append(float(nnn[0]))

range_absc=[i for i in col if i >= a and i <= b]
c=range_absc[0]
d=range_absc[-1]
c_idx=col.index(c)
d_idx=col.index(d)


files=["xanes_x.dat", "xanes_75deg.dat", "xanes_60deg.dat", "xanes_45deg.dat", "xanes_20deg.dat", "xanes_z.dat"]

for arq in files:
    temp1=open(arq,"r")
    lines=temp1.readlines()[4:]
    sigma=[]
    peaks=[]
    for line in lines:
        cols=line.split()
        sigma.append(float(cols[1]))
    peaks=[peak for idx, peak in enumerate(sigma) if idx >= c_idx and idx <= d_idx]
    mm=max(peaks)
    maximum.append(mm)
    temp1.close()

#dumb1=sigma[c_idx]
#dumb2=sigma[d_idx]

#maximum=max(peaks)

print(c, c_idx)
print(d, d_idx)
#print(dumb1, dumb2)
print("The maximum values are: ", maximum)

absc=list(sss)
print("Sine function on angle vs intensity: ", absc, maximum)

kkk=dict(zip(absc, maximum))
for i, j in kkk.items():
    to_file=print(round(i, 4), "   ", round(j, 4))
    
    
f.close()
