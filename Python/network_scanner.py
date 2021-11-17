import scapy.all as scapy 

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    #arp_request.show()
    #scapy.arping(ip)
    #print(arp_request.summary())
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    #broadcast.show()
    arp_request_broadcast = broadcast/arp_request
    #print(arp_request_broadcast)
    answered_lis = scapy.srp(arp_request_broadcast, timeout=1)[0]

    print("IP\t\t\tMAC Addrres\n-----------------------------------------")

    for element in answered_lis:
        #print(element[1].show()) # todos 
        # informacipon detallada

        print(element[1].psrc + "\t\t" + element[1].hwsrc)

        #print(element[1].psrc)
        #print(element[1].hwsrc)
        print("------------------------------------------")

scan("192.168.1.1/24")