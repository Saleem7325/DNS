import socket

def LS():
    try:
        ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[LS]: Server socket created")
    except socket.error as err:
        print("[LS]: socket open error: {}\n".format(err))
        exit()

    server_binding = ('', 50006)
    ls.bind(server_binding)
    ls.setblocking(False)
    ls.listen(1)

    host = socket.gethostname()
    print("[LS]: Server hostname is {}".format(host))

    localhost_ip = (socket.gethostbyname(host))
    print("[LS]: Server IP address is {}".format(localhost_ip))

    csockid, addr = ls.accept()
    print ("[LS]: Got a connection request from a client at {}".format(addr))

    data_from_client = csockid.recv(100)
    print ("[LS]: Data from client: {}".format(data_from_client.decode("UTF-8")))

    # Send data from client to TS1
    port = 50007
    localhost_addr = socket.gethostbyname(socket.gethostname())
    server_binding = (localhost_addr, port)
    ls.connect(server_binding)
    ls.send(data_from_client)

LS()