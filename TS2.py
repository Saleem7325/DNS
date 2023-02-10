import socket

def TS2():
    try:
        ts2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[TS2]: Server socket created")
    except socket.error as err:
        print("[TS2]: socket open error: {}\n".format(err))
        exit()

    server_binding = ('', 50008)
    ts2.bind(server_binding)
    ts2.listen(1)

    host = socket.gethostname()
    print("[TS2]: Server hostname is {}".format(host))

    localhost_ip = (socket.gethostbyname(host))
    print("[TS2]: Server IP address is {}".format(localhost_ip))

    table = {}

    f = open("PROJ2-DNSTS2.txt")
    lines = f.readlines()
    for line in lines:
        hostname = line.split()[0]
        table[hostname] = line.strip()
        print("[TS2]: {}: {}".format(hostname, table[hostname]))


TS2()