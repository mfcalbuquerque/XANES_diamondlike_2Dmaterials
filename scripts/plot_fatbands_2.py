import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

fermi_abc_sc=[0.0037, 0.0145]
fermi_abc_A1=[-2.5832, -2.6326] # scf and nscf fermi levels
fermi_abc_A2=[-2.5697, -2.6144] # scf and nscf fermi levels
###
fermi_aba_B1=[-2.9040, -2.8797]
fermi_abc_B2=[-2.9294, -2.9138]  
shift=284.2


fat_abc_sc=pd.read_fwf('bands_abc_sc')
pdos_abc_sc=pd.read_fwf('pdos_abc_sc')
fat_abc_A1=pd.read_fwf('bands_abc-B2_p')
pdos_abc_A1=pd.read_fwf('pdos_abc_B2')

###########
###########

#fat_abc_uc=pd.read_fwf('bands_abc_uc')
#fat_abc_sc=pd.read_fwf('bands_abc_sc')
#pdos_abc_uc=pd.read_fwf('pdos_abc_uc')
#pdos_abc_sc=pd.read_fwf('pdos_abc_sc')

#print(fat_aba.head(100))
#print(dfg.head(100))



fat_abc_sc['energy']=fat_abc_sc['energy'] - fermi_abc_sc[0] + shift        # Fermi level is provided.
fat_abc_A1['energy']=fat_abc_A1['energy'] - fermi_abc_B2[0] + shift        # Fermi level is provided.
pdos_abc_sc['energy']=pdos_abc_sc['energy'] - fermi_abc_sc[-1] + shift        # Fermi level is provided.
pdos_abc_A1['energy']=pdos_abc_A1['energy'] - fermi_abc_B2[-1] + shift        # Fermi level is provided.
pdos_abc_sc['P-PDOS']=pdos_abc_sc['P-PDOS']/54
pdos_abc_sc['S-PDOS']=pdos_abc_sc['S-PDOS']/54
pdos_abc_A1['P-PDOS']=pdos_abc_A1['P-PDOS']/54
pdos_abc_A1['S-PDOS']=pdos_abc_A1['S-PDOS']/54
#dfg.energy=dfg.energy+shift                         # Energy is shifted up to the value of the Carbon K-core-level (284.2 eV).
#######
#######
#fat_abc_uc['energy']=fat_abc_uc['energy'] - fermi_abc_uc[0] + shift        # Fermi level is provided.
#fat_abc_sc['energy']=fat_abc_sc['energy'] - fermi_abc_sc[0] + shift        # Fermi level is provided.
#pdos_abc_uc['energy']=pdos_abc_uc['energy'] - fermi_abc_uc[-1] + shift        # Fermi level is provided.
#pdos_abc_sc['energy']=pdos_abc_sc['energy'] - fermi_abc_sc[-1] + shift        # Fermi level is provided.
#pdos_abc_uc['P-PDOS']=pdos_abc_uc['P-PDOS']/6
#pdos_abc_uc['S-PDOS']=pdos_abc_uc['S-PDOS']/6
#pdos_abc_sc['P-PDOS']=pdos_abc_sc['P-PDOS']/54
#pdos_abc_sc['S-PDOS']=pdos_abc_sc['S-PDOS']/54


bands_xlim=[0.0, 1.58]
pdos_xlim=[0.0, 0.25]
ylim=[305.00,306.0]

fig, ((ax1,ax2), (ax3,ax4)) = plt.subplots(2, 2, figsize=(15,10)) #, constrained_layout=True)
#fig, ax = plt.subplots(figsize=(15,12))


fat_abc_sc.plot(x='kpts', y='energy', kind='scatter', c='P-orbitals', cmap='summer', grid=True, ax=ax1)
fat_abc_sc.plot(x='kpts', y='energy', grid=True, c='black', ax=ax1, linewidth='0.3', legend='')
ax1.set_ylabel('Energy (eV)')
ax1.set_xlabel('')
ax1.set_xticks([0.00, 0.6666, 0.9999, 1.5773])
ax1.set_xticklabels(['$\Gamma$','K','M','$\Gamma$'])
ax1.set_ylim(ylim)
ax1.set_xlim(bands_xlim)
ax1.hlines(y=shift, xmin=0.0, xmax=1.5773, colors='DimGray', linestyles='dashed') #, linewidth=2.0)
#ax1.legend(loc='upper center', bbox_to_anchor=(1.11, 1.0))
#ax.annotate('ABA', (1.55, 305))
#ax1_set_axhline(y=284.2, color='DimGray', linstyle='--', linewidth='2.0')
###############
pdos_abc_sc.plot(x='S-PDOS', y='energy', kind='line', ax=ax2, grid=True, color='green', label='unit cell: s')
pdos_abc_sc.plot(x='P-PDOS', y='energy', kind='line', ax=ax2, grid=True, color='yellow', label='unit cell: p')
ax2.set_xlabel('PDOS (states/[eV.per etom])')
ax2.set_ylabel('Energy (eV)')
ax2.set_ylim(ylim)
ax2.set_xlim(pdos_xlim)
ax2.hlines(y=shift, xmin=pdos_xlim[0], xmax=pdos_xlim[1], colors='DimGray', linestyles='dashed') #, linewidth=2.0)
#ax2.annotate('ABC', (1.55, 305))
################
fat_abc_A1.plot(x='kpts', y='energy', kind='scatter', c='P-orbitals', cmap='summer', grid=True, ax=ax3)
fat_abc_A1.plot(x='kpts', y='energy', grid=True, color='black', ax=ax3, linewidth='0.3', legend='')
ax3.set_ylabel('Energy (eV)')
ax3.set_xlabel('')
ax3.set_xticks([0.00, 0.6671, 1.0008, 1.5788])
ax3.set_xticklabels(['$\Gamma$','K','M','$\Gamma$'])
ax3.set_ylim(ylim)
ax3.set_xlim(bands_xlim)
ax3.hlines(y=shift, xmin=0.0, xmax=1.5788, colors='DimGray', linestyles='dashed') #, linewidth=2.0)
#############
#############
pdos_abc_A1.plot(x='S-PDOS', y='energy', kind='line', ax=ax4, grid=True, color='green', label='ABC-B2: s')
pdos_abc_A1.plot(x='P-PDOS', y='energy', kind='line', ax=ax4, grid=True, color='yellow', label='ABC-B2: p')
ax4.set_xlabel('PDOS (states/[eV.per etom])')
ax4.set_ylabel('Energy (eV)')
ax4.set_ylim(ylim)
ax4.set_xlim(pdos_xlim)
ax4.hlines(y=shift, xmin=pdos_xlim[0], xmax=pdos_xlim[1], colors='DimGray', linestyles='dashed') #, linewidth=2.0)
#############
#############
############
plt.tight_layout()
#plt.show()
plt.savefig('plot_abc_B2_305-306.pdf')
