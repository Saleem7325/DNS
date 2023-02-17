import socket
import sys

def TS1():
    if len(sys.argv) < 2:
        print("[C]: Need to provide ts1ListenPort")
        exit()

    try:
        port = int(sys.argv[1])
    except ValueError:
        print("[C]: ts1ListenPort must be a numeric value")
        exit()

    try:
        ts1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[TS1]: Server socket created")
    except socket.error as err:
        print("[TS1]: socket open error: {}\n".format(err))
        exit()

    server_binding = ('', port)
    ts1.bind(server_binding)
    ts1.listen(1)

    host = socket.gethostname()
    print("[TS1]: Server hostname is {}".format(host))

    localhost_ip = (socket.gethostbyname(host))
    print("[TS1]: Server IP address is {}".format(localhost_ip))

    table = {}

    f = open("PROJ2-DNSTS1.txt")
    lines = f.readlines()
    for line in lines:
        hostname = line.split()[0].lower()
        table[hostname] = line.strip()

    lssockid, addr = ts1.accept()
    print ("[TS1]: Got a connection request from a client at {}".format(addr))

    while True:
        data_from_client = lssockid.recv(200).decode("UTF-8").lower()
        if data_from_client:
            print("[TS1]: data from client: {}".format(data_from_client))
            if table.has_key(data_from_client):
                lssockid.send(table[data_from_client] + " IN".encode("UTF-*"))
        else:
            break

TS1()

