# SolaxCloud to Domoticz
Get inverter data from Solax Cloud using API to the Domoticz
# Note
Solax Cloud data are refresed every 5 min. 

# Installation

1. Clone code

```
cd /home/pi
git clone https://github.com/diggahpl/SolaxCloud_to_Domoticz.git
```

2. Configure script, add API token, dongle SN, and Domoticz URL

```
vim /home/pi/SolaxCloud_to_Domoticz/solaxcloud-to-domoticz.py

change : 

myapitoken = 'XXX' # API token to get form SolaxCloud user menu
mydonglesn = 'XXX' # Registration no./ module SN
domoticzurl = '192.168.2.191:8080' # Domoticz IP and port

```

3. Create Domoticz Dummy Hardware (Setup/Hardware)


4. Create three Domoticz Virtual Sensor Devices (Setup/Hardware/Create Virtual Sensors)

  * TotalPower	 (Type Usage, Subtype Electric)
  * DailyPower (Type Usage, Subtype Electric)
  * AC power  (Type Usage, Subtype Electric)

5. Take a note of your Domoticz devices IDX numbers and adjust `solaxcloud-to-domoticz.py` id_= values respectively, lines 19 to 21 for Solax X3 MIC inverter  .

6. Finally add cronjob triggered Python script that will fetch data from SolaxCloud and push into Domoticz

Either `crontab -e` for pi user

```
*/1 * * * * /home/pi/SolaxCloud-to-domoticz/solaxcloud-to-domoticz.py | logger
```

or add this as a system cronjob

```
echo "*/1 * * * * root /home/pi/SolaxCloud-to-domoticz/solaxcloud-to-domoticz.py | logger" > /etc/cron.d/solaxcloud-to-domoticz
```

# This script is based on 

``
https://github.com/zmielna/smogomierz-to-domoticz
```
