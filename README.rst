==================================================================================================
High precision ECG Database with annotated R peaks, recorded and filmed under realistic conditions
==================================================================================================

This is an API which provides transparent online access to the ECG GUDB
http://researchdata.gla.ac.uk/716/ without the need of downloading it.

It contains ECGs from 25 subjects. Each subject was recorded performing 5 different tasks for two minutes:
   * sitting
   * a maths test on a tablet
   * walking on a treadmill
   * running on a treadmill
   * using a hand bike

The following channels were recorded with two Attys (https://www.attys.tech/) running synchronously:
   * Einthoven II and III with standard cables and the amplifier worn around the waist
   * Exercise cheststrap ECG which resembles approximtely V2-V1 with the ECG amplifier directly mounted on the strap
   * Acceleration in X/Y/Z whith the sensor mounted directly on the chest strap
   
The cheststrap ECG allowed R peak detection even while jogging at a
very high precision (+/- one sample). The sampling rate was 250Hz at a
resolution of 24 bits. The database contains the unfiltered,
DC-coupled signals as originally recorded. In order to be able to link
the ECG artefacts to the behaviour of the subject all but one subject
gave permission to be filmed and the videos are also part of the
database.



Installation
============

Simply install via pip or pip3::

   pip install ecg_gudb_database
   pip3 install ecg_gudb_database


   
Usage
=====

Check out `usage_example.py` on github which plots the ECG and the heartrate of one subject.


Module
------

The module is called `ecg_gudb_database`::

    from ecg_gudb_database import GUDb


The constructor loads the ECG data of one subject and one experiment from github::

    ecg_class = GUDb(subject_number, experiment)

where `subject_number` is from 0..24 and `experiment` is 'sitting', 'maths', 'walking', 'hand_bike' or 'jogging'.
The array `ecg_class.experiments` contains these names so that one can loop through the different experiments.

Retrieve the ECG data
---------------------

The data is available as numpy arrays. The sampling rate is 250Hz for all experiments (`ecg_class.fs`).
we have recorded Einthoven and from a chest strap.

Einthoven::

    ecg_class.einthoven_I, ecg_class.einthoven_I_filt
    ecg_class.einthoven_II, ecg_class.einthoven_II_filt
    ecg_class.einthoven_III, ecg_class.einthoven_III_filt


Chest strap::

    ecg_class.cs_V2_V1, ecg_class.cs_V2_V1_filt

where the filtered versions have 50Hz mains and DC removed.


R peak annotations
------------------

The two boolean variables `ecg_class.anno_cs_exists` and `ecg_class.anno_cables_exists`
tell the user if annotations exist. If yes they can be obtained::


    if ecg_class.anno_cs_exists:
        chest_strap_anno = ecg_class.anno_cs
    else:
        print('No chest strap annotations')
    if ecg_class.anno_cables_exists:
        cables_anno = ecg_class.anno_cables
    else:
        print("No cables annotations")



Videos
======

Where the participant has consented, there is a video for each of the tasks.
The video and ECG data have been synchronised so they start and end at the same time. The videos can be requested here:

http://researchdata.gla.ac.uk/716/
