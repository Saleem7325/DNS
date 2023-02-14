import socket
import errno
import select

def client():
    try:
        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[C]: Client socket created")
    except socket.error as err:
        print('socket open error: {} \n'.format(err))
        exit()

    # Define the port on which you want to connect to the server
    port = 50006
    localhost_addr = socket.gethostbyname(socket.gethostname())

    # connect to the server on local machine
    server_binding = (localhost_addr, port)
    cs.connect(server_binding)
    # cs.setblocking(0)

    # Send string to server
    # msg = "This is a message"
    # print("[C]: Data sent to server: {}".format(msg))
    # cs.send(msg.encode('UTF-8'))

    f = open("PROJ2-HNS.txt")
    lines = f.readlines()
    total = 0
    for line in lines:
        hostname = line.strip()
        print("[S]: Data send to server: {} ".format(hostname))
        cs.send(hostname.encode("UTF-8"))
        data_from_server = cs.recv(100).decode("UTF-8")
        print("[S]: Data from server: {} ".format(data_from_server))
        # while len(hostname):
        #     try:
        #         sent = cs.send(hostname.encode("UTF-8"))
        #         total += sent
        #         hostname = hostname[sent:]
        #     except socket.error as e:
        #         if e.errno != errno.EAGAIN:
        #             raise e
        #         select.select([], [cs], [])

            
        



client()