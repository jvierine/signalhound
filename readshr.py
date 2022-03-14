import numpy as n
import sys
import os
import matplotlib.pyplot as plt



class shr_read:
    def __init__(self,fname,plot=False):
        self.fname=fname
        self.f=open(fname,"r")
        shr_header=n.dtype([('signature', n.uint16),
                            ('version', n.uint16),
                            ('res', n.uint32),
                            ('dataOffset',n.uint64),
                            ("sweep_count",n.uint32),
                            ("sweep_length",n.uint32),
                            ("first_bin_freq_Hz",n.float64),
                            ("bin_size_Hz",n.float64),
                            ("title",(n.uint16,128)),
                            ("center_freq_hz",n.float64),
                            ("span_Hz",n.float64),
                            ("rbw_Hz",n.float64),
                            ("vbw_Hz",n.float64),
                            ("ref_lev_dBm",n.float32),
                            ("ref_scale",n.uint32),
                            ("div",n.float32),
                            ("window",n.int32),
                            ("attenuation",n.int32),
                            ("gain",n.int32),
                            ("detector",n.int32),
                            ("processing_units",n.int32),
                            ("window_bandwidth",n.float64),
                            ("decimation_type",n.int32),
                            ("decimation_det",n.int32),
                            ("decimation_count",n.int32),
                            ("decimation_time_ms",n.int32),
                            ("chanellize_enabled",n.int32),
                            ("chanel_output_unitss",n.int32),
                            ("chanel_center_freq",n.float64),
                            ("chanel_width_Hz",n.float64),
                            ("reserved2",n.uint32)])
        
        
        shr_sweep_header=n.dtype([('timestamp', n.uint64),
                                  ('lat', n.float64),
                                  ('lon', n.float64),
                                  ('alt', n.float64),
                                  ('overflow', n.uint8),
                                  ('reserved', (n.uint8,15))])
        

        z=n.fromfile(self.f,dtype=shr_header,count=1)
        byte_offset=z["dataOffset"][0]
        self.sweep_length=z["sweep_length"][0]
        self.sweep_count=z["sweep_count"][0]
        
        self.first_bin_hz=z["first_bin_freq_Hz"][0]
        self.bin_size_hz=z["bin_size_Hz"][0]
        self.freqs=n.arange(self.sweep_length)*self.bin_size_hz + self.first_bin_hz
        
        self.f.seek(byte_offset, os.SEEK_SET)

        self.S=n.zeros(self.sweep_length)
        self.n_avg=0.0
        for swi in range(self.sweep_count):
            swh=n.fromfile(self.f,dtype=shr_sweep_header,count=1)
            sweep=n.fromfile(self.f,dtype=n.float32,count=self.sweep_length)
            self.S+=sweep
            self.n_avg+=1.0
            #plt.plot(self.freqs/1e6,sweep)
            #plt.show()
            #print(z)
            #print(swh)
        self.S=self.S/self.n_avg
        if plot:
            plt.plot(self.freqs/1e6,self.S)
            plt.show()


if __name__ == "__main__":
    s=shr_read(sys.argv[1],plot=True)


                                                        
