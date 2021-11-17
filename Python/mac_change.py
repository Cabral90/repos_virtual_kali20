#!/usr/bin/env python
import subprocess
#rint("--------  CONSULTANDO LOS DATOS DE LA NET -------")
#subprocess.call("ifconfig", shell=True) # consultamos
print("--------  APAGANDO LA NET -------")
subprocess.call("ifconfig eth0 down", shell=True) # apagar la net
print("--------  CAMBIANDO LA MAC -------")
subprocess.call("ifconfig eth0 hw ether 00:11:22:33:44:66", shell=True) # nueva mac
print("--------  ARRANCANDO LA NET -------")

subprocess.call("ifconfig eth0 down", shell=True) # arrancar la net la maqui

print("--------  CONSULTANDO LOS DATOS DE LA NET -------")
subprocess.call("ifconfig", shell=True) # consultamos