###############################################################################
# client-python.py
# Name: Llewnosuke Priimak
# EID: lp27636
###############################################################################

import sys
import socket

SEND_BUFFER_SIZE = 2048


def read_large_message(chunk_size=1024):

    while True:
        chunk = sys.stdin.read(chunk_size)
        if not chunk:
            break
        yield chunk


def client(server_ip, server_port):

    """TODO: Open socket and send message from sys.stdin"""


    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_ip,server_port))
    while True:

        for chunk in read_large_message():
            s.send(chunk.encode('UTF-8'))

        break
    s.close()



def main():


    """Parse command-line arguments and call client function """
    if len(sys.argv) != 3:
        sys.exit("Usage: python client-python.py [Server IP] [Server Port] < [message]")

    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])
    client(server_ip, server_port)

if __name__ == "__main__":
    main()
