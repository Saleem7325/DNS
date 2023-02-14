import socket

def TS1():
    try:
        ts1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[TS1]: Server socket created")
    except socket.error as err:
        print("[TS1]: socket open error: {}\n".format(err))
        exit()

    server_binding = ('', 50007)
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
        # print("[TS1]: {}: {}".format(hostname, table[hostname]))

    lssockid, addr = ts1.accept()
    print ("[TS1]: Got a connection request from a client at {}".format(addr))

    # data_from_client = lssockid.recv(100)
    # print ("[TS1]: Data from LS: {}".format(data_from_client.decode("UTF-8")))

    while True:
        data_from_client = lssockid.recv(200).decode("UTF-8").lower()
        if data_from_client:
            print("[TS1]: data from client: {}".format(data_from_client))
            if table.has_key(data_from_client):
                lssockid.send(table[data_from_client].encode("UTF-*"))
        else:
            break;

TS1()

