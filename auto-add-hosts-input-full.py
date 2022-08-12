#!/usr/bin/env python
# -*- coding: utf-8 -*-

#author: Franco Ferraciolli

from getpass import getpass
  
serverurl = input("Informe a URL de acesso do Zabbix : " )
username = input("Informe o usuario para acesso a API : " )
senha = getpass("Informe a senha : " )

from pyzabbix import ZabbixAPI
import csv
from progressbar import ProgressBar, Percentage, ETA, ReverseBar, RotatingMarker, Timer

zapi = ZabbixAPI(serverurl)
zapi.login(user=username, password=senha)

arq = csv.reader(open(r"C:\Users\FrancoFerraciolli\OneDrive - Telic Technologies\1 [MONITORAMENTO] API-ZABBIX SCRIPTS PARA ADICAO DE HOSTS\auto_add_hosts\HOST-ARQUIVOS\hosts1.csv"))

linhas = sum(1 for linha in arq)

f = csv.reader(open(r"C:\Users\FrancoFerraciolli\OneDrive - Telic Technologies\1 [MONITORAMENTO] API-ZABBIX SCRIPTS PARA ADICAO DE HOSTS\auto_add_hosts\HOST-ARQUIVOS\hosts1.csv"), delimiter=';')
bar = ProgressBar(maxval=linhas,widgets=[Percentage(), ReverseBar(), ETA(), RotatingMarker(), Timer()]).start()
i = 0

for [hostname,ip,community,tagvalue1,tagvalue2] in f:
    hostcriado = zapi.host.create(
        host= hostname,
        inventory_mode = 0,
        status= 1,
        interfaces = [{
            "type": 2,
            "main": 1,
            "useip": 1,
            "ip": ip,
            "dns": "",
            "port": 161,
            "details": {
                "version": 2,
                "bulk": 0,
                "community": community
            }
        }],
        groups = [{
            "groupid": "32"
        }],
        tags = [{
            "tag": "equipamento",
            "value": tagvalue1},
            {"tag": "monitoramento",
            "value": tagvalue2
        }],
        templates = [{
            "templateid": 10186
        }]
    )


    i += 1
    bar.update(i)

bar.finish
print (" ")
