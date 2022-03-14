import readshr as rs

import matplotlib.pyplot as plt



open_pa=rs.shr_read("/data1/nya/na_march13_train/pa_thermal_test_pa_no_load2022-03-13 09h11m55s.shr")
load_pa=rs.shr_read("/data1/nya/na_march13_train/pa_thermal_test_on2022-03-13 08h36m55s.shr")
load_nopa=rs.shr_read("/data1/nya/na_march13_train/pa_thermal_test_pa_off_load2022-03-13 09h04m17s.shr")
ant=rs.shr_read("/data1/nya/na_march13_train/pa_thermal_test_antenna2022-03-13 09h32m40s.shr")
cabin2=rs.shr_read("/data1/nya/na_march11_cabin2/pa2022-03-11 08h15m53s.shr")


plt.plot(open_pa.freqs/1e6,open_pa.S,label="Preamp on, open load")
plt.plot(load_pa.freqs/1e6,load_pa.S,label="Preamp on, 50 ohm load")
plt.plot(load_nopa.freqs/1e6,load_nopa.S,label="Preamp off, 50 ohm load")
plt.plot(ant.freqs/1e6,ant.S,label="Preamp on, antenna connected")
plt.plot(cabin2.freqs/1e6,cabin2.S,label="Cabin 2")
plt.xlabel("Frequency (MHz)")
plt.ylabel("Power (dBm)")
plt.legend()
plt.tight_layout()
plt.show()
