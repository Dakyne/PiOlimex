#!/usr/bin/python3.7
import datetime
import openeeg
#import pyqtgraph as pg
#from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
#import threading
#import pyqtgraph.multiprocess as mp
import time
print("Starting EEG reader")


data1 = np.ones((1024,), dtype=np.int)*512
data2 = np.ones((1024,), dtype=np.int)*512

openeeg.eeg_init();
fout = open('/home/pi/data/record.dat','w');
freq = 2
while True:
    update = 0
    eeg_vals = openeeg.eeg_get();
    if eeg_vals:
        eeg_vals = filter(None,eeg_vals.split('X'))
        for eeg_val in eeg_vals:
            fout.write(eeg_val);
            fout.write('\n')
            fout.flush();
            ch1 = eeg_val.split(' ')[0];
            ch2 = eeg_val.split(' ')[1];
            data1 = np.roll(data1,-1)
            data2 = np.roll(data2,-1)
            if update % freq == 0:
                data1[1023] = ch1;
                data2[1023] = ch2;
            update += 1
            #print data1
fout.close();
openeeg.eeg_destroy();

