import numpy as n
import glob
import matplotlib.pyplot as plt
import scipy.signal as ss



#fl=glob.glob("/data1/nya/na_march11_cabn2_iq/*.iq")


#fl=glob.glob("/data1/nya/na_march11_cabin1_iq/*.iq")
fl=glob.glob("/data1/nya/march11_iq_french/*.iq")

fl.sort()
print(len(fl))
n_fft=65536

wf=ss.hann(n_fft)
S=n.zeros(n_fft)
fvec= n.fft.fftshift(n.fft.fftfreq(n_fft,d=1.0/40e6))
for fi,f in enumerate(fl):
    print(f)
    S[:]=0.0
    z=n.fromfile(f,dtype="<i2")
    ns=len(z)/2
    z=n.array(z[n.arange(ns,dtype=n.int)*2]+1j*z[n.arange(ns,dtype=n.int)*2+1],dtype=n.complex64)

    n_w = int(n.floor(len(z)/n_fft))
    n_avg=0.0
 #   print(n_w)
    for wi in range(n_w):
        peak_amp=n.max(n.abs(z[ (wi*n_fft):(wi*n_fft+n_fft)]))
        #        print(peak_amp)
        #       if peak_amp < 10e3:
        #        print(wi)
        S+=n.abs(n.fft.fftshift(n.fft.fft(wf*z[ (wi*n_fft):(wi*n_fft+n_fft)])))**2.0
        n_avg+=1.0
    S=S/n_avg
    S.tofile("%s.spec"%(f))
#    if fi%500==0:
 #       plt.plot(fvec/1e6+100.0,10.0*n.log10(S))
  #      #   plt.xlim([95,105])
        # plt.ylim([105,120])
   #     plt.xlabel("Frequency (MHz)")
    #    plt.ylabel("Power (dB)")
     #   plt.show()

#plt.plot(fvec/1e6+100.0,10.0*n.log10(S))
#plt.xlabel("Frequency (MHz)")
#plt.ylabel("Power (dB)")
#plt.show()
        
    
