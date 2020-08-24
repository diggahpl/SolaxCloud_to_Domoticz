#!/usr/bin/python3
import json, urllib.request, codecs


# -------- SoluxCloud config
#
myapitoken = 'XXX' # API token to get form SolaxCloud user menu
mydonglesn = 'XXX' # Registration no./ module SN
#
# -------- Domoticz config
#
domoticzurl = '192.168.2.191:8080' # Domoticz IP and port
#
#
# -------- Domoticz IDX section
#
id_inverterSN = '' # Domoticz IDX for inverterSN
id_sn = '' # Domoticz IDX for sn
id_acpower = '51' # Domoticz IDX for acpower
id_yieldtoday = '50' # Domoticz IDX for yieldtoday in kW
id_yieldtotal = '49' # Domoticz IDX for yieldtotal in kW
id_feedinpower = '' # Domoticz IDX for feedinpower
id_feedinenergy = '' # Domoticz IDX for feedinenergy 
id_consumeenergy = '' # Domoticz IDX for consumeenergy 
id_feedinpowerM2 = '' # Domoticz IDX for feedinpowerM2
id_soc = '' # Domoticz IDX for soc
id_peps1 = '' # Domoticz IDX for peps1
id_peps2 = '' # Domoticz IDX for peps2
id_peps3 = '' # Domoticz IDX for peps3
id_inverterType = '' # Domoticz IDX for inverterType
id_inverterStatus = '' # Domoticz IDX for inverterStatus
id_uploadTime = '' # Domoticz IDX for uploadTime
id_success = '' # Domoticz IDX for success
#
# --------- Magic starts here
soluxcloudurl = 'https://www.eu.solaxcloud.com:9443/proxy/api/getRealtimeInfo.do?tokenId='+myapitoken+'&sn='+mydonglesn+'' # Create URL with token and SN

response = urllib.request.urlopen(soluxcloudurl)
reader = codecs.getreader("utf-8")
responseDictionary = json.load(reader(response)) 
SoluxData = responseDictionary["result"] # get only results from JSON response 

domoticzurl_yieldtotal  = 'http://%s/json.htm?type=command&param=udevice&idx=%s&nvalue=0&svalue=%s' % (domoticzurl,id_yieldtotal, SoluxData["yieldtotal"]*1000) # yieldtotal in Watt
domoticzurl_yieldtoday  = 'http://%s/json.htm?type=command&param=udevice&idx=%s&nvalue=0&svalue=%s' % (domoticzurl,id_yieldtoday, SoluxData["yieldtoday"]*1000) # yieldtoday in Watt
domoticzurl_acpower  = 'http://%s/json.htm?type=command&param=udevice&idx=%s&nvalue=0&svalue=%s' % (domoticzurl,id_acpower, SoluxData["acpower"]) # acpower in Watt 

urls = [domoticzurl_yieldtotal, domoticzurl_yieldtoday, domoticzurl_acpower] 

for url in urls:
    urllib.request.urlopen(url)
