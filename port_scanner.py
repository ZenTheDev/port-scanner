#!/usr/bin/env python3
try:
    from traceback import print_exc
except:
    print('Something went wrong importing the traceback module...')
    input('\033[91mMake sure to report this bug to the developer!\033[0m')
loadASCII, index, port, openPorts, currentThread, serverIP, speed, portMin, portMax = ['--', '\\', '|', '/'], -1, 1, [], 0, str(), float(), 0, 1
try:
    from threading import Thread, enumerate
    from time import sleep
    from socket import socket, gethostbyname, gaierror, error, timeout, AF_INET, SOCK_STREAM
    from ipaddress import IPv4Address
    from datetime import datetime
    from sys import stdout
    from os import system as sys

    sys('')
except:
    print('Something went wrong while importing certain modules for the scanner...')
    print('\033[91mMake sure to report this bug to the developer, \033[4m\033[1mwith the traceback!\033[0m\n')
    print_exc()
    input()
def scanPort(_serverIP, _port, _index):
    print(f"Scanning port no. \033[32m{_port}\033[0m... \033[34m{loadASCII[_index]}\033[0m")
    sock = socket(AF_INET, SOCK_STREAM)  # Creates socket with IPv4 address family and stream type
    sock.settimeout(0.5)  # Timeout of 5s
    res = sock.connect_ex((_serverIP, _port))  # Creates connection
    if res == 0:  # If port is open
        openPorts.append(_port)
    sock.close()  # Closes the socket
def scanServerPorts():
    try:
        n1 = datetime.now()
        global index, port, openPorts, currentThread
        index, port, openPorts, currentThread = -1, 1, [], 0

        def createConnection(remoteServer):
            try:
                global port, openPorts, serverIP, index
                try: IPv4Address(remoteServer)
                except: serverIP = gethostbyname(remoteServer)  # Retrieves server internet protocol
                else: serverIP = remoteServer
                port = portMin
                while port < portMax:
                    index += 1  # Incrementing index to show loading ascii art
                    if index == 4:
                        index = 0
                    exec("t = Thread(target=scanPort, args=(serverIP, port, index,)); t.start()")  # Creates new thread
                    port += 1
                    try: sleep(float(speed))
                    except: sleep(0.005)
                sys("CLS")
                for openPort in openPorts:
                    print(f"\033[36m{openPort}\033[0m is open.")  # Logs which ports are open
            except gaierror:  # Host name is invalid
                print("Unresolvable host name...")
                input("Press any key to continue")
            except timeout:  # Socket timed out
                print("Session timed out...")
                input("Press any key to continue")
            except error:  # Connection unavailable
                print("Unable to connect to host...")
                input("Press any key to continue")
            except Exception:  # Something else went wrong
                print("Something went wrong while initiating new threads probably...")
                print_exc()
                input("Press any key to continue")

        host = input("Enter the Host IP/Name: ")

        def speedInput():
            global speed
            speed = input("Enter the delay mode (slow, med, fast, ultra, null, custom i.e: '.023'), for help type '?': ")
            if speed == '?':
                print("\n\033[1m\033[38;5;208mslow:\033[0m "
                      + "has a delay of \033[1m0.05\033[0m, not recommended but very accurate.\n"
                      + "\033[1m\033[38;5;226mmed:\033[0m "
                      + "has a delay of \033[1m0.02\033[0m, okay but should mainly be used if you have a bad ISP or if you want more accurate results.\n"
                      + "\033[1m\033[38;5;118mfast:\033[0m "
                      + "has a delay of \033[1m0.005\033[0m, this is very recommended, as it shouldn't cause much lag but it is faster than usual and somewhat accurate.\n"
                      + "\033[1m\033[38;5;63multra:\033[0m "
                      + "has a delay of \033[1m0.003\033[0m, anything more and it might glitch, this should only be used with a good "
                      + "computer and connection, this isn't very accurate and will likely skip a few open ports.\n"
                      + "\033[1m\033[38;5;124mnull:\033[0m "
                      + "has \033[1m\033[38;5;196mno delay\033[0m, highly unrecommended, has a much higher chance of crashing or glitching, if you want to use this"
                      + ", you might wanna have a super computer\n")
                speedInput()
            if str(speed).lower() == "slow":
                speed = .05
            elif str(speed).lower() == "med":
                speed = .02
            elif str(speed).lower() == "fast":
                speed = .005
            elif str(speed).lower() == "ultra":
                speed = .003
            elif str(speed).lower() == 'null':
                speed = 0
            else:
                speed = float(speed)

        def portInput():
            portNum = input("Enter the range of ports that you want to scan, for help type '?': ")
            if portNum.lower() == '?':
                print("\nEnter the minimum argument then maximum argument like this: \033[38;5;226m\033[1mmin max\033[0m\n")
                portInput()
            elif int(portNum.split(' ')[0]) >= int(portNum.split(' ')[1]):
                print("\n\033[38;5;208m\033[1mMinimum integer\033[0m should not be higher than \033[1mmaximum integer\033[0m!\n")
                portInput()
            elif int(portNum.split(' ')[1]) > 65535:
                print("\n\033[38;5;208mCan not go higher than the limit of \033[1m65535\033[0m!\n")
                portInput()
            else:
                global portMin, portMax
                portMin = int(portNum.split(' ')[0])
                portMax = int(portNum.split(' ')[1])

        speedInput()
        portInput()
        sys("CLS")

        createConnection(host)

        n2 = datetime.now()

        print(f"Time taken: {-(n1 - n2).total_seconds()}s")  # Logs how long it took

        uchoice_loop = input("Type 'loop' to continue, just press enter to exit: ")
        if uchoice_loop.lower() == 'loop':
            sys("CLS")
            scanServerPorts()
    except:
        print('Something went wrong while initializing the scanner...')
        print('\033[91mMake sure to report this bug to the developer, \033[4m\033[1mwith the traceback!\033[0m\n')
        print_exc()
        input()
scanServerPorts()
