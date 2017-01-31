import numpy as np
from LDC4005 import LDC4005
from PM100 import PM100


set_current = np.linspace(0, 0.02, 20)

measure_current = np.zeros(len(set_current))
measure_voltage = np.zeros(len(set_current))
measure_power = np.zeros(len(set_current))

# usbtmc0 odpadawia ldc, a usbtmc1 pm100
ldc = LDC4005("/dev/usbtmc0")
pm100 = PM100("/dev/usbtmc1")

pm100.set_wavelength_in_nm(635)
ldc.on()

for i in range(0, len(set_current)):
    ldc.set_ld_current_in_amper(set_current[i])
    measure_current[i] = ldc.ld_current_reading()
    measure_voltage[i] = ldc.ld_voltage_reading()
    measure_power[i] = pm100.get_power()

np.savetxt("dane.txt", np.c_[measure_current, measure_voltage, measure_power]
, fmt='%1.16f', header="current [A] \t voltage [V] \t power [W]")
