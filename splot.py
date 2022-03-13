import numpy as n
import glob
import matplotlib.pyplot as plt
import stuffr

fl=glob.glob("/data1/nya/na_march11_cabn2_iq/*.spec")
#fl=glob.glob("/data1/nya/na_march11_cabin1_iq/*.spec")
#fl=glob.glob("/data1/nya/march11_iq_french/*.spec")

fl.sort()
n_fft=65536
n_file=len(fl)

freq=n.fft.fftshift(n.fft.fftfreq(n_fft,d=1.0/40e6))+100e6
fidx=n.where( (freq>87e6) & (freq<112e6) )[0]

fdec=614
dt=0.1875
f2=stuffr.decimate(freq[fidx],dec=fdec)
tdec=10
n_t=int(len(fl)/tdec)
AS=n.zeros([n_t,len(f2)],dtype=n.float32)

n_f=len(fl)


for ti in range(n_t):
    for di in range(tdec):
        f=fl[ti*tdec + di]
        print(f)
        S=n.fromfile(f,dtype=n.float64)
        #n_fft=len(S)
        #    plt.plot(freq[fidx]/1e6,S[fidx])
        #   plt.show()
        AS[ti,:]+=stuffr.decimate(S[fidx],dec=fdec)
        print(len(fidx))
#    plt.plot(freq/1e6,10.0*n.log10(S))
 #   plt.show()
  #  print(f)

plt.pcolormesh(f2/1e6,n.arange(n_t)*dt*tdec,10.0*n.log10(AS))
plt.xlabel("Frequency (MHz)")
plt.ylabel("Time (seconds)")

cb=plt.colorbar()
cb.set_label("Power (dB)")
plt.show()

  
ASD=10.0*n.log10(AS)
for fi in range(len(f2)):
    ASD[:,fi]=ASD[:,fi]-n.median(ASD[:,fi])
plt.pcolormesh(f2/1e6,tdec*dt*n.arange(n_t),ASD,vmin=-.2)
plt.xlabel("Frequency (MHz)")
plt.ylabel("Time (seconds)")

cb=plt.colorbar()
cb.set_label("Power (dB)")
plt.show()

