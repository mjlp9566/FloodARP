# FloodARP
An ARP flooding tool that disconnects communication for everyone from your local network except you.

<h3>How it works?</h3>

`ARP` (Address Resolution Protocol) is used for the translation of IP address to MAC address. But why this translation is needed? because our transmitted packets will reach the target system's Network Interface Card (NIC). The NICs only have MAC(physical) address, we use IP address for communication which is being used for the unique identification of Hosts at network level. while the packets are reaching the physical layer it needs the MAC address of the NIC.

Let's say you want to communicate with a computer having IP address (192.168.44.45) in your LAN. Your computer will broadcast a ARP request asking that who-has the IP (192.168.44.45) and the computer having the IP address will give a response that 192.168.44.55 is-at MAC-address of the target computer.
![image](https://github.com/mjlp9566/FloodARP/assets/55002003/1eff26c5-6e38-4e0e-ad35-5d2056e06f2c)

The tool get IP of yout gateway as input and send a ARP reply that the gateway IP is at your's MAC address , so all the hosts in the LAN will send the frames to you and no frames will reach the gateway but still all the computers are connected to the network.

<h3>Usage</h3>

Clone the repository

```
git clone https://github.com/mjlp9566/FloodARP.git
```

Install the requirements

```
pip install -r requirements.txt
```

Run the tool and give your gateway IP

```
python FloodARP.py
```

To find the gateway IP in **Linux** - `ip r` and in **Windows** - `ipconfig`
![image](https://github.com/mjlp9566/FloodARP/assets/55002003/335909f1-a624-438e-a339-671048521908)

![image](https://github.com/mjlp9566/FloodARP/assets/55002003/fcc901e1-0b20-4be0-a65c-8e69c059467a)

<h3>Screenshots</h3>

Attacker - Kali linux
Victim   - Santoku 

<h4>Before attack:</h4>
The MAC address of the gateway before the attack

![image](https://github.com/mjlp9566/FloodARP/assets/55002003/e560013d-ca9d-4e64-878b-030bcd15d31b)

Internet connectivity before attack

![image](https://github.com/mjlp9566/FloodARP/assets/55002003/aa9480ca-1a5c-4b60-b97c-c050b3b616d8)

<h4>After Attack:</h4>
The MAC adderss is changed as the Attacker's MAC address

![image](https://github.com/mjlp9566/FloodARP/assets/55002003/301fb8c8-a6a6-4e35-a1e5-d9455cd1c570)

Internet connectivity is lost

![image](https://github.com/mjlp9566/FloodARP/assets/55002003/97315768-4bd1-4c3b-9011-7279e1ac9ce0)

<h3>Mitigation</h3>

> Configure Static ARP entry for the gateway.



