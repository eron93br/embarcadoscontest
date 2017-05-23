# Embarcados Contest - Inventando o Futuro com DragonBoard 410C

[Debian Guide for DragonBoard](http://builds.96boards.org/releases/dragonboard410c/linaro/debian/16.09/)

biblioteca MRAA (libmraa): irá disponibilizar um meio de acessar pinos I/O em várias linguagens! 

- GPS

Using the onboard GPS

The GPS software stack mostly runs on the DSP subsystem. The communication between the main CPU and the DSP is done with a specific IPC driver called QRTR (see ./net/qrtr/ in the kernel source tree). Because of bug 416, the DSP is not started automatically at boot. To start the GPS, the DSP needs to be started first. Once the DSP is started any gpsd client can be started and will be able to retrieve GPS data.

Please note that the sensitivity of the onboard antenna is quite low, so getting a FIX will take several minutes. Please refer to the dedicated application note to install an external antenna for better GPS performance.

To get started with GPS, first install the following packages:

sudo apt-get install gpsd-clients gnss-gpsd

The package gnss-gpsd will bring all the needed dependencies to use the onboard GPS. Then you need to start the DSP:

sudo systemctl start qdsp-start.service

From now on, you can use any gpsd client, such as gpsmon or xgps.

- Linux User Guide

[User Guide](https://github.com/96boards/documentation/blob/master/ConsumerEdition/DragonBoard-410c/Guides/LinuxUserGuide_DragonBoard.pdf)
