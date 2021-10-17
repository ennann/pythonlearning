# from flask import Flask
# app = Flask(__name__)
# # Flask is uppercase, means it's a object.
#
# @app.route('/')
# def hello_world():
#     return 'Hello, World!'
#
#
from l_03_functions import create_devices
from datetime import datetime

t = str(datetime.utcnow())
print(type(t))

devices = create_devices(3)
print(type(devices))

device = dict()
print(type(device))


from scapy.all import *
target = '192.168.2.11'
ans, unans = sr(IP(dst = target) / TCP(sport = RandShort(), dport = [22, 80, 123], flags = "S"), timeout = 5)
for sent, received in ans:
        if received.haslayer(TCP) and str(received[TCP].flags) == "SA":
                print "Port " + str(sent[TCP].dport) + " of " + target + " is OPEN!"
        elif received.haslayer(TCP) and str(received[TCP].flags) == "RA":
                print "Port " + str(sent[TCP].dport) + " of " + target + " is closed!"
        elif received.haslayer(ICMP) and str(received[ICMP].type) == "3":
                print "Port " + str(sent[TCP].dport) + " of " + target + " is filtered!"
for sent in unans:
        print str(sent[TCP].dport) + " is filtered!"