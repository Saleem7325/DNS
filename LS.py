import errno
import socket
import select

def LS():
    try:
        ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ts1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ts2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[LS]: Server socket created")
    except socket.error as err:
        print("[LS]: socket open error: {}\n".format(err))
        exit()

    # Bind socket to port 5006 
    server_binding = ('', 50006)
    ls.bind(server_binding)
    ls.listen(1)
    # ls.setblocking(0)

    host = socket.gethostname()
    print("[LS]: Server hostname is {}".format(host))

    localhost_ip = (socket.gethostbyname(host))
    print("[LS]: Server IP address is {}".format(localhost_ip))

    # Accept connection from client
    # select.select([ls], [], [])
    csockid, addr = ls.accept()
    print ("[LS]: Got a connection request from a client at {}".format(addr))

    # Receive data from client
    # data_from_client = csockid.recv(100)
    # print ("[LS]: Data from client: {}".format(data_from_client.decode("UTF-8")))

    # Send data from client to TS1
    port = 50007
    localhost_addr = socket.gethostbyname(socket.gethostname())
    ts1_binding = (localhost_addr, port)
    ts1.connect(ts1_binding)
    ts1.setblocking(0)
    # ts1.send(data_from_client)

    # Send data from client to TS1
    port = 50008
    ts2_binding = (localhost_addr, port)
    ts2.connect(ts2_binding)
    ts2.setblocking(0)
    # ts2.send(data_from_client)

    while True:
        data_from_client = csockid.recv(200).decode("UTF-8")
        if data_from_client:
            print("[LS]: data from client: {}".format(data_from_client))

            total = 0
            data = data_from_client
            while len(data):
                try:
                    sent = ts1.send(data.encode("UTF-8"))
                    total += sent
                    data = data[sent:]
                except socket.error as e:
                    if e.errno != errno.EAGAIN:
                        raise e
                    select.select([], [ts1], [])
                
            total = 0
            data = data_from_client
            while len(data):
                try:
                    sent = ts2.send(data.encode("UTF-8"))
                    total += sent
                    data = data[sent:]
                except socket.error as e:
                    if e.errno != errno.EAGAIN:
                        raise e
                    select.select([], [ts2], [])

            reading, writing, exception = select.select([ts1, ts2], [], [], 5)

            if reading:
                response = reading[0].recv(100)
                csockid.send(response)
            else:
                csockid.send((data_from_client + " - TIMED OUT").encode("UTF-8"))

            
            # ts1.send(data_from_client)
            # ts2.send(data_from_client)
        else:
            break;
            

LS()