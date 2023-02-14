import socket
import errno
import select
import sys

def client():
    if len(sys.argv) < 3:
        print("[C]: Need to provide lsHostname and lsListenPort")
        exit()

    try:
        port = int(sys.argv[2])
    except ValueError:
        print("[C]: lsListenPort must be a numeric value")
        exit()
    
    lsHostName = sys.argv[1]

    try:
        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[C]: Client socket created")
    except socket.error as err:
        print('socket open error: {} \n'.format(err))
        exit()

    # Define the port on which you want to connect to the server
    # port = 50006
    # localhost_addr = socket.gethostbyname(socket.gethostname())
    lsHostname_addr = socket.gethostbyname(lsHostName)

    # connect to the server on local machine
    # server_binding = (localhost_addr, port)
    server_binding = (lsHostname_addr, port)
    cs.connect(server_binding)


    f = open("PROJ2-HNS.txt")
    r = open("RESOLVED.txt", "w")
    lines = f.readlines()
    total = 0
    for line in lines:
        hostname = line.strip()
        print("[C]: Data sent to server: {} ".format(hostname))
        cs.send(hostname.encode("UTF-8"))
        data_from_server = cs.recv(100).decode("UTF-8")
        print("[C]: Data from server: {} ".format(data_from_server))
        r.write(data_from_server + "\n")


            
        



client()