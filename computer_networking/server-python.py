###############################################################################
# server-python.py
# Name: Llewnosuke Priimak
# EID: lp27636
###############################################################################

import sys
import socket
import threading

RECV_BUFFER_SIZE = 2048
QUEUE_LENGTH = 10
#PORT = 50008
HOST = ''
ADDRESS = '127.0.0.1'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def thread(client_socket):

    while True:

        info = client_socket.recv(RECV_BUFFER_SIZE)
        info = info.decode("UTF-8")
        if len(info) > 0:
            print(info)
        elif len(info) <= 0:
            break

    print("Connection to client closed")
    client_socket.close()


def server(server_port):


    # """TODO: Listen on socket and print received message to sys.stdout"""
    # // listen to the port using socket functionality
    # // inifinite loop, because always listen to the client unless the user ctrl-C
    # // once you receive a client
    # // process the client request
    # // multithread will happen
    # // each thread will process the client request or data in parallel
    # // once the post processing is done, the thread will die or exit

    s.bind((ADDRESS,server_port))
    s.listen(QUEUE_LENGTH)
    print("SERVER UP LISTENING FOR CLIENTS")

    while(True):


        (socketForClient, clientIP) = s.accept()
        print(f'Connected to : {clientIP[0]} : {clientIP[1]}')

        threader = threading.Thread(target = thread, args = (socketForClient,))
        threader.start()



def main():


    """Parse command-line argument and call server function """
    if len(sys.argv) != 2:
        sys.exit("Usage: python server-python.py [Server Port]")
    server_port =int(sys.argv[1])
    server(server_port)

if __name__ == "__main__":
    main()