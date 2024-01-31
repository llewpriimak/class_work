# Import socket module
import socket
import sys




def read_large_message(chunk_size=1024):
    # message = sys.stdin.read()
    # print(message)

    #print(chunk)
    while True:
        chunk = sys.stdin.read()
        if not chunk:
            break
        yield chunk


def main():


    """Parse command-line arguments and call client function """
    # if len(sys.argv) != 3:
    #     sys.exit("Usage: python client-python.py [Server IP] [Server Port] < [message]")

    # message = sys.stdin.read()
    #read_large_message()
    for i in read_large_message():
        print(i)


if __name__ == "__main__":
    main()