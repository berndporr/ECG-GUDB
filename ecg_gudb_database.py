"""
(C) 2018-2020 Bernd Porr <bernd.porr@glasgow.ac.uk>
(C) Luis Howell <2123374H@student.gla.ac.uk>

GNU GENERAL PUBLIC LICENSE
Version 3, 29 June 2007

API for the data which loads, filters and exports
the ECG data.
"""

import numpy as np
import scipy.signal as signal
import io
import requests

# Class which loads the dataset
class GUDb:

    experiments = ["sitting","maths","walking","hand_bike","jogging"]
    fs=250
    total_subjects = 25
    url = "https://berndporr.github.io/ECG-GUDB/experiment_data"

    def loadDataFromURL(self,url):
        s=requests.get(url).content
        c=np.loadtxt(io.StringIO(s.decode('utf-8')))
        return c
    
    def __init__(self,_subj,_experiment):
        """ Constructor: Specify the subject number and the experiment"""
        self.subj = _subj
        self.experiment = _experiment
        self.subjdir = self.url+"/"+("subject_%02d" % _subj)+"/"
        self.expdir = self.subjdir+self.experiment+"/"

        self.data=self.loadDataFromURL(self.expdir+"ECG.tsv")
        try:
            self.anno_cs=self.loadDataFromURL(self.expdir+"annotation_cs.tsv").astype(int)
            self.anno_cs_exists=True 
        except:
            self.anno_cs=False
            self.anno_cs_exists=False           
        try:
            self.anno_cables=self.loadDataFromURL(self.expdir+"annotation_cables.tsv").astype(int)
            self.anno_cables_exists=True 
        except:
            self.anno_cables=False
            self.anno_cables_exists=False   

        self.cs_V2_V1 = self.data[:, 0]
        self.einthoven_II = self.data[:, 1]
        self.einthoven_III = self.data[:, 2]
        self.einthoven_I = self.einthoven_II - self.einthoven_III
        self.acc_x = self.data[:, 3]
        self.acc_y = self.data[:, 4]
        self.acc_z = self.data[:, 5]

        self.T=1/self.fs
        self.t = np.linspace(0, self.T*len(self.cs_V2_V1), len(self.cs_V2_V1))


    def filter_data(self):
        """Filters the ECG data with a highpass at 0.1Hz and a bandstop around 50Hz (+/-2 Hz)"""

        b_dc, a_dc = signal.butter(4, (0.1/self.fs*2), btype='highpass')
        b_50, a_50 = signal.butter(4, [(48/self.fs*2),(52/self.fs*2)], btype='stop')

        self.cs_V2_V1_filt = signal.lfilter(b_dc, a_dc, self.cs_V2_V1)
        self.cs_V2_V1_filt = signal.lfilter(b_50, a_50, self.cs_V2_V1_filt)

        self.einthoven_II_filt = signal.lfilter(b_dc, a_dc, self.einthoven_II)
        self.einthoven_II_filt = signal.lfilter(b_50, a_50, self.einthoven_II_filt)

        self.einthoven_III_filt = signal.lfilter(b_dc, a_dc, self.einthoven_III)
        self.einthoven_III_filt = signal.lfilter(b_50, a_50, self.einthoven_III_filt)

        self.einthoven_I_filt = self.einthoven_II_filt-self.einthoven_III_filt

        return
