# -*- coding: utf-8 -*-

#author: Franco Ferraciolli
  
import dotenv
import os
import csv
from pyzabbix import ZabbixAPI
from progressbar import ProgressBar, Percentage, ETA, ReverseBar, RotatingMarker, Timer

dotenv.load_dotenv(dotenv.find_dotenv())
TOKEN = os.getenv("api_token")

zapi = ZabbixAPI("http://161.35.60.64")
zapi.login(api_token=TOKEN)

arq = csv.reader(open(r"C:\Users\Franco\Documents\TESTES API ZABBIX PYTHON\hosts_teste_add.csv"))

linhas = sum(1 for linha in arq)

f = csv.reader(open(r"C:\Users\Franco\Documents\TESTES API ZABBIX PYTHON\hosts_teste_add.csv"), delimiter=';')
bar = ProgressBar(maxval=linhas,widgets=[Percentage(), ReverseBar(), ETA(), RotatingMarker(), Timer()]).start()
i = 0

for [hostname,ip,tagvalue,desc] in f:
    hostcriado = zapi.host.create(
        host= hostname,
        inventory_mode = 0,
        status= 0,
        interfaces = [{
            "type": 1,
            "main": 1,
            "useip": 1,
            "ip": ip,
            "dns": hostname,
            "port": 10050,
        }],
        groups = [{
            "groupid": "60"
        }],
        tags = [{
            "tag": "tag_tpt_pcp",
            "value":tagvalue
        }],
        description = desc   
    )

    i += 1
    ##bar.update(i)
    print(hostname +';'+ hostcriado['hostids'][0])
    #with open('deposito.csv', 'w', newline='\r\n', encoding='utf-8') as f:
       # writer = csv.writer(f)
       # writer.writerow([hostname , hostcriado['hostids'][0]])

#bar.finish
print (" ")