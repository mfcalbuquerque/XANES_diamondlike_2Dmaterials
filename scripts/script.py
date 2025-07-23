import numpy as np
from matplotlib import pyplot as plt
import pandas as pd


f=pd.read_csv('kkk_2proj.csv', sep='\s+')

x=f.energy
x2=f.energy + 284.2

#print(f.head())
#print(x.head())
#print(x2.head())
#print(f.aba_x.head())
#y_max=max(f.aba_z)
#y1=f.aba_x / y_max
#y2=f.aba_z / y_max
#y3=f.abc_x / y_max
#y4=f.abc_z / y_max
#y5=f.aaa_x / y_max
#y6=f.aaa_z / y_max

#print(y1.head())
plt.subplot(2,2,1)
#ax1.margins()
plt.plot(x2, f.aba_x, label='ABA-'r'$\bot$', color='DeepSkyBlue')
plt.plot(x2, f.abc_x, label='ABC-'r'$\bot$', color='Blue')
plt.plot(x2, f.aaa_x, label='AAA-'r'$\bot$', color='Navy')
plt.axvline(x=284.2, color='green', linestyle='--', lw='1.0')
plt.xlim((280.0, 310.0))
plt.xlabel('Energy (eV)')
plt.ylabel(r'$\sigma$'' (arb. units)')
plt.legend(loc='upper right', fontsize='x-small')

plt.subplot(2,2,2)
#ax2.margins()
plt.plot(x2, f.aba_z, label='ABA-//', color='LightSalmon')
plt.plot(x2, f.abc_z, label='ABC-//', color='Crimson')
plt.plot(x2, f.aaa_z, label='AAA-//', color='DarkRed')
plt.axvline(x=284.2, color='green', linestyle='--', lw='1.0')
plt.xlim((280.0, 310.0))
plt.xlabel('Energy (eV)')
plt.ylabel(r'$\sigma$'' (arb. units)')
plt.legend(loc='upper right', fontsize='x-small')

plt.subplot(2,1,2)
#ax3.margins()
plt.plot(x2, f.aba_x, label='ABA-'r'$\bot$', color='DeepSkyBlue')
plt.plot(x2, f.abc_x, label='ABC-'r'$\bot$', color='Blue')
plt.plot(x2, f.aaa_x, label='AAA-'r'$\bot$', color='Navy')
plt.plot(x2, f.aba_z, label='ABA-//', color='LightSalmon')
plt.plot(x2, f.abc_z, label='ABC-//', color='Crimson')
plt.plot(x2, f.aaa_z, label='AAA-//', color='DarkRed')
plt.axvline(x=284.2, color='green', linestyle='--', lw='1.0')
plt.xlim((280.0, 310.0))
plt.xlabel('Energy (eV)')
plt.ylabel(r'$\sigma$'' (arb. units)')
plt.legend(loc='upper right', fontsize='x-small')

plt.tight_layout()

plt.show()


#plt.plot(x2, y1, label='ABA-'r'$\bot$', color='DeepSkyBlue')
#plt.plot(x2, y3, label='ABC-'r'$\bot$', color='Blue')
#plt.plot(x2, y5, label='AAA-'r'$\bot$', color='Navy')
#plt.plot(x2, y2, label='ABA-//', color='LightSalmon')
#plt.plot(x2, y4, label='ABC-//', color='Crimson')
#plt.plot(x2, y6, label='AAA-//', color='DarkRed')
#
#plt.axvline(x=284.2, color='green', linestyle='--', lw='1.0')
#
#plt.xlim((280.0, 310.0))
#
#plt.xlabel('Energy (eV)')
#plt.ylabel(r'$\sigma$'' (arb. units)')
#
#plt.legend()
#plt.show()
