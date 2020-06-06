"""
(C) Luis Howell <2123374H@student.gla.ac.uk>
(C) 2018-2020 Bernd Porr <bernd.porr@glasgow.ac.uk>

GNU GENERAL PUBLIC LICENSE
Version 3, 29 June 2007

Example how to use the API
"""

from ecg_gudb_database import GUDb
import matplotlib.pyplot as plt
import pathlib
import numpy as np


#function for plotting ecg data, annotations are optional
def plot_ecg(axs, t, data, anno = []):

    axs.plot(t, data)
    if len(anno)>0:
        axs.plot(t[anno], data[anno], 'ro')
    
    axs.set_ylabel('Chest ECG/V')
    axs.set_xlabel('Time (s)')

    
#function for plotting acc data
def plot_acc(axs, t, x,y,z):

    axs.plot(t,x, t,y, t,z)
    axs.set_ylabel('Acceleration m/s2^2')
    axs.set_xlabel('Time (s)')

    
# plots the heartrate
def plot_hr(axs, fs, anno):
        
    intervals = np.diff(anno)
    heart_rate = 60.0/(intervals/float(fs))
    var = np.diff(heart_rate)
    
    time = anno * (1.0/fs)
    
    axs.plot(time[1:], heart_rate)
    axs.set_ylabel('Heart rate / BPM')
    axs.set_xlabel('Time (s)')


    
#subject number to load, starting at 0
subject_number = 0

#print experiments
print("Experiments:", GUDb.experiments)

#experiment to load
experiment = 'jogging'

# creating class which loads the experiment
ecg_class = GUDb(subject_number, experiment)


#getting the raw ECG data numpy arrays from class
chest_strap_V2_V1 = ecg_class.cs_V2_V1
einthoven_i = ecg_class.einthoven_I
einthoven_ii = ecg_class.einthoven_II
einthoven_iii = ecg_class.einthoven_III

#getting filtered ECG data numpy arrays from class
ecg_class.filter_data()
chest_strap_V2_V1_filt = ecg_class.cs_V2_V1_filt
einthoven_i_filt = ecg_class.einthoven_I_filt
einthoven_ii_filt = ecg_class.einthoven_II_filt
einthoven_iii_filt = ecg_class.einthoven_III_filt

#getting annotations
if ecg_class.anno_cs_exists:
    chest_strap_anno = ecg_class.anno_cs
else:
    print('No chest strap annotations')
if ecg_class.anno_cables_exists:
    cables_anno = ecg_class.anno_cables
else:
    print("No cables annotations")

fig, axs = plt.subplots(4, 1)

fig.suptitle('Subject %02d: %s' % (subject_number, experiment))

axs[0].plot(ecg_class.t, einthoven_ii_filt)
axs[0].set_ylabel('Einthoven II/V')
axs[0].set_xlabel('Time (s)')

#plotting the chest strap data with annotations
plot_ecg(axs[1],ecg_class.t, chest_strap_V2_V1, anno=chest_strap_anno)

#if we have R peak annotations then let's plot the heartrate
if ecg_class.anno_cs_exists:
    plot_hr(axs[2],ecg_class.fs,chest_strap_anno)

plot_acc(axs[3],ecg_class.t,ecg_class.acc_x,ecg_class.acc_y,ecg_class.acc_z)


plt.show()
