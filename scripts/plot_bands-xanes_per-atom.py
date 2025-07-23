import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

num=7.0302
shift=284.2


df=pd.read_fwf('fatbands-atoms')
dfg=pd.read_fwf('xanes')

#print(df.head(100))
#print(dfg.head(100))



df.energy=df.energy-num        # Fermi level is provided.
dfg.energy=dfg.energy+shift      # Energy is shifted up to the value of the Carbon K-core-level (284.2 eV).
df.energy=df.energy+shift

#fig,axes=plt.subplots(nrows=1, ncols=3, figsize=(20,8), constrained_layout=True)
#
#df.plot(x='kpts', y='energy', kind='scatter', c='projx', cmap='plasma') #, ax=axes[0,0], grid=True)
#axes[0,0].set_ylabel('Energy (eV)')
#axes[0,0].set_xlabel('')
#axes[0,0].set_xticks([0.00, 0.6665, 0.9998, 1.5771])
#axes[0,0].set_xticklabels(['$\Gamma$','K','M','$\Gamma$'])
#################
#df.plot(x='kpts', y='energy', kind='scatter', c='projz', cap='plasma') #, ax=axes[0,1], grid=True)
#axes[0,1].set_xlabel('')
#axes[0,1].set_ylabel('Energy (eV)')
#axes[0,1].set_xticks([0.00, 0.6665, 0.9998, 1.5771])
#axes[0,1].set_xticklabels(['$\Gamma$','K','M','$\Gamma$'])
#################
#dfg.plot(x='energy', y=['sigmax','sigmaz'], ax=axes[0,2], legend=True, grid=True)
##dfg.plot(x='energy', y='sigmaz', ax=axes[0,2], legend=False, grid=True)
#axes[0,2].set_xlabel('Energy (eV)')
#axes[0,2].set_ylabel('$\sigma$ (arb. units)')
##axes[0,2].set_label((''r'$\bot$','//')
##
#################
##df.plot(kind='scatter', x='kpts', y='energy', c='2py', colormap='plasma', ax=axes[1,1], grid=True)
##axes[1,1].set_xlabel('')
##axes[1,1].set_ylabel('Energy (eV)')
##axes[1,1].set_xticks([0.00, 0.67, 1.00, 1.58])
##axes[1,1].set_xticklabels(['$\Gamma$','K','M','$\Gamma$'])
#################
##plt.tight_layout()
#plt.show()



fig, (ax1,ax2,ax3) = plt.subplots(1, 3, figsize=(20,6)) #, constrained_layout=True)

df.plot(x='kpts', y='energy', kind='scatter', c='$P_x$', cmap='Blues', ax=ax1, grid=True)
ax1.set_ylabel('Energy (eV)')
ax1.set_xlabel('')
ax1.set_xticks([0.00, 0.6665, 0.9998, 1.5771])
ax1.set_xticklabels(['$\Gamma$','K','M','$\Gamma$'])
ax1.set_ylim([280,310])
ax1.set_xlim([0.0,1.58])
ax1.hlines(y=shift, xmin=0.0, xmax=1.5771, colors='DimGray', linestyles='dashed') #, linewidth=2.0)
#cb1=fig.colorbar(sp1, ax=ax1)
#cb1.set_label('2px')
#ax1_set_axhline(y=284.2, color='DimGray', linstyle='--', linewidth='2.0')
################
df.plot(x='kpts', y='energy', kind='scatter', c='$P_z$', cmap='Oranges', ax=ax2, grid=True)
ax2.set_xlabel('')
ax2.set_ylabel('Energy (eV)')
ax2.set_xticks([0.00, 0.6665, 0.9998, 1.5771])
ax2.set_xticklabels(['$\Gamma$','K','M','$\Gamma$'])
ax2.set_ylim([280,310])
ax2.set_xlim([0.0,1.58])
ax2.hlines(y=shift, xmin=0.0, xmax=1.5771, colors='DimGray', linestyles='dashed') #, linewidth=2.0)
################
dfg.plot(x='energy', y=['sigmax','sigmaz'], label=['ABC: 'r'$\bot$','ABC: //'], ax=ax3, legend=True, grid=True)
#dfg.plot(x='energy', y='sigmaz', ax=axes[0,2], legend=False, grid=True)
ax3.set_xlabel('Energy (eV)')
ax3.set_ylabel('$\sigma$ (arb. units)')
ax3.vlines(x=shift, ymin=0, ymax=0.18, colors='DimGray', linestyles='dashed') #, linewidth=2.0)
ax3.set_xlim([280,310])
ax3.set_ylim([0.0,0.180])
#axes[0,2].set_label((''r'$\bot$','//')
#
################
#df.plot(kind='scatter', x='kpts', y='energy', c='2py', colormap='plasma', ax=axes[1,1], grid=True)
#axes[1,1].set_xlabel('')
#axes[1,1].set_ylabel('Energy (eV)')
#axes[1,1].set_xticks([0.00, 0.67, 1.00, 1.58])
#axes[1,1].set_xticklabels(['$\Gamma$','K','M','$\Gamma$'])
################
plt.tight_layout()
plt.show()
