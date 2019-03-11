# This script runs on Python 3
#ROOTSEC
#HUB: https://r00ts3c.github.io/
#DISCORD: https://discord.gg/G6tfGDD
import socket, threading
import sys
import logging
def TCP_connect(ip, port_number, delay, output):
    TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    TCPsock.settimeout(delay)
    try:
        TCPsock.connect((ip, port_number))
        output[port_number] = 'Listening'
    except:
        output[port_number] = ''



def scan_ports(host_ip, delay):

    threads = []        # To run TCP_connect concurrently
    output = {}         # For printing purposes
    
    # Spawning threads to scan ports
    logging.debug('appending threads')
    for i in range(500):
        
        t = threading.Thread(target=TCP_connect, args=(host_ip, i, delay, output))
        threads.append(t)
        
    # Starting threads
    logging.debug('finished appending')
    for i in range(500):
            try:
                logging.debug('starting thread %s', threads[i])
                threads[i].start()
            except RuntimeError:
                   print("Run time error:", sys.exc_info()[0])
                   raise

    # Locking the script until all threads complete
    for i in range(500):
        threads[i].join()

    # Printing listening ports from small to large
    for i in range(500):
        if output[i] == 'Listening':
            print(str(i) + ': ' + output[i])

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] (%(threadName)-10s) %(message)s',)

def run(target):
    host_ip = target
    delay = int(input("How many seconds the socket is going to wait until timeout: "))
    print(target)
    scan_ports(host_ip, delay)


def main():
   
    host_ip = input("Enter host IP: ")
    delay = int(input("How many seconds the socket is going to wait until timeout: "))   
    scan_ports(host_ip, delay)

if __name__ == "__main__":
    main()
