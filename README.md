# MMS-protocol-attacks

<h2>Aim of the project </h2>
List of cybersecurity attacks on client and server MMS under TLS.
I realised these attacks during my intership in the university in collaboration with Ricerca sul Sistema Energetico(RSE spa).

<h2>Technologies </h2>
<li> Docker and containers </li>
<li> Transport Layer Security(TLS) </li>
<li> Manufacturing Message Specification(MMS) protocol</li>

<h2> Experimentation  </h2>
<li> Search for vulnerabilities in the TLS protocol and main cipher suites </li>
<li> Search for security attacks </li>
<li> Search for tools </li>
<li> Run the attacks</li>

<h2> Developed attacks </h2>
<li> Passive Man-in-the-middle </li>
<li> Denial of service </li>
<li> Packet filtering </li>
<li> Downgrade </li>


<h1> Launch attacks </h1>

<h2> Run Client and Server </h2>
<p> 
  Terminal1 <code> ./serverexec  </code> 
  <br>
  Terminal2  <code> ./clientexec </code> 

<br>
  Terminal1  <code> ./start </code>
  <br>
  Terminal2  <code> ./start [SERVER_IP] </code>  (Example : <code>  ./start 172.17.0.3 </code> )

</p>

<h2> Passive Man in the Middle</h2>


<p>
  <strong> Run client and server first! </strong><br>
Terminal3 (arp)  <code>  ./arp </code>   <br>
Terminal4 (tcpdump)  <code> ./tcpdump </code>  <br>
Terminal3 (arp)  <code>  ./start [SERVER_IP] [CLIENT_IP]  </code>    (Example : <code>  ./start 172.17.0.3 172.17.0.2 </code> ) <br>
Terminal4 (tcpdump)  <code> ./start </code>  <br>
Terminal1  <code> ./start </code>
</p>

<h2> WebSocket Denial of Service </h2>
<p>
  <strong> Run client and server first! </strong><br>
Terminal3  (dos) <code>  ./dosattack </code>  <br>
Terminal3  (dos) <code>  ./start [IP_SERVER] </code>  <br>
Terminal1  <code> ./start </code>

 </p>
  
<h2> Packet Filtering </h2>
<p>
  <strong> Run client and server first! </strong><br>

Terminal3 (packetfilter) <code> ./packetfilter</code>   <br>
Terminal4 (arp) <code> ./arp </code>  <br>
Terminal4 (arp) <code> ./start [IP_SERVER] [IP_CLIENT]</code>  <br>

Then run one of these two scripts:
• Terminal3(packetfilter) <code> ./start_inject </code> <br>
• Terminal3 (packetfilter)<code> ./start_pending </code> <br>
 </p>
 
