# MQTT message router for Jeedom/ESP ECU #

[ESP ECU](https://github.com/patience4711/read-APSystems-YC600-QS1-DS3/wiki) publish all messages in a single topic.
Jeedom [JMQTT plugin](https://domotruc.github.io/jMQTT/fr_FR/) required a dedicated topic per virtual device.

This router will republish the message to a topic named after the inverter serial.

based on ESP ECU message format v4.
```
{"inv_serial":"703000159999","freq":50.0,"temp":26.9,"acv":230.5,"ch0":[43.9,1.6,62.6,244.98],"ch1":[23.4,0.0,0.0,0.00],"totals":[62.6,244.98]}
```

Sample JMQTT device template is provided (APS DS3 with 2 MPTT)

## Installation instructions (for use with jeedom) ##

The following commands will install the MQTT router and automatically start it upon jeedom restart.

```
sudo su -
cd /home/jeedom
git clone https://github.com/kaneda-fr/MQTT-Router-ESP-ECU.git
ln -s MQTT-Router-ESP-ECU/mqtt-router.service /etc/systemd/system/mqtt-router.service
systemctl enable mqtt-router 
systemctl start mqtt-router 
```
