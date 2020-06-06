# High precision ECG Database with annotated R peaks, recorded and filmed under realistic conditions

This is an API which accesses the database here: http://researchdata.gla.ac.uk/716/

This database contains ECGs from 25 subjects. Each subject was recorded performing 5 different tasks for two minutes:
   * sitting
   * a maths test on a tablet
   * walking on a treadmill
   * running on a treadmill
   * using a hand bike

The following channels were recorded with two [Attys](https://www.attys.tech/) running synchronously:
   * Einthoven II and III with standard cables and the amplifier worn around the waist
   * Exercise cheststrap ECG which resembles approximtely V2-V1 with the ECG amplifier directly mounted on the strap
   * Acceleration in X/Y/Z whith the sensor mounted directly on the chest strap
   
The cheststrap ECG allowed R peak detection even while jogging at a very high precision (+/- one sample). The sampling rate was 250Hz at a resolution of 24 bits. The database contains the unfiltered, DC-coupled signals as originally recorded. In order to be able to link the ECG artefacts to the behaviour of the subject all but one subject gave permission to be filmed and the videos are also part of the database.





## Videos

Where the participant has consented, there is a video for each of the tasks. The video and ECG data have been synchronised so they start and end at the same time. The videos can be requested here:

http://researchdata.gla.ac.uk/716/
