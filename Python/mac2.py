import subprocess # processos de comando de Shell
import optparse
from typing import Optional # importar comandos 



parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest = "interface", help="Interface para Cambiar Direccion MAC")
parser.add_option("-m", "--mac", dest = "new_mac", help="Nueva Direccion MAC")

(options, arguments) = parser.parse_args()

"""
OBS: shell=True es un defecto error de programacion porque puede recibir mas de un comando de inputo separado por comas

subprocess.call("ifconfig " + interface + " down", shell=True) 
subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True) 
subprocess.call("ifconfig " + interface + " up", shell=True) 
"""

# interface= input("interface ejemplo [eth0] > ")
# new_mac= input("Neuvo MAC ejemplo: [00:11:22:33:44:67] > ")

interface= options.interface
new_mac= options.new_mac

# PROBANDO: sudo python3 mac2.py --interface < name_interface > --mac < new_direction_mac >
# PROBANDO: sudo python3 mac2.py --interface eth0 --mac 00:11:22:33:44:99

print("[+] Cambiando Direccion de MAC para "+interface + " a "+ new_mac)
# mas segura 
subprocess.call(["ifconfig", interface, "down"]) 
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac]) 
subprocess.call(["ifconfig", interface, "up"]) 