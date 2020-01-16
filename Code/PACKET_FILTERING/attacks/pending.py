#!/usr/bin/python3
from netfilterqueue import NetfilterQueue
from scapy.all import *

nfQueueID         = 0
maxPacketsToStore = 100
count =0
def packetReceived(pkt):
  global count
  count+=1
  print("=====PACCHETTO n. ",count, "=======")
  
  test="x02"
 
  
  print("T:",test)
  
  macadd = str(pkt.get_hw())
  
 # print(".SPLIT:" ,macadd.split("\\")[5])
  split = macadd.split("\\")[5]
  boolhost = test==split
  if(boolhost and count> 27):
  #Se si volesse filtrare per dimensione (byte)
  #if(pkt.get_payload_len()==1500): 
    pkt.drop()
    print("DROPPED", pkt.get_payload_len())
    return
  print("Accepted a new packet...")
  print(pkt)
  
  print("ADDRESS", pkt.get_hw())
  ip = IP(pkt.get_payload())
  if not ip.haslayer("Raw"):
    pkt.accept();
    print("Non RAW")
  else:
    tcpPayload = ip["Raw"].load;
   
    msgBytes = pkt.get_payload()       # msgBytes is read-only, copy it
    print("Lunghezza: ",len(msgBytes))
    
    pkt.accept();

print("Binding to NFQUEUE", nfQueueID)
nfqueue = NetfilterQueue()
nfqueue.bind(nfQueueID, packetReceived, maxPacketsToStore) # binds to queue 0, use handler "packetReceived()"
try:
    nfqueue.run()
except KeyboardInterrupt:
    print('Listener killed.')

nfqueue.unbind()

