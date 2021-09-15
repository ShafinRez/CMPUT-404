import socket, time, sys 
from multiprocessing import Process

HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def get_remote_ip(host):
    print(f'Getting IP for {host}')
    try:
        remote_ip = socket.gethostbyname( host )
    except socket.gaierror:
        print ('Hostname could not be resolved. Exiting')
        sys.exit()

    print (f'Ip address of {host} is {remote_ip}')
    return remote_ip

def handle_request():

    return


def main():
    HOST = 'www.google.com'
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_start:
        proxy_start.bind((HOST, PORT))
        proxy_start.listen()
        conn, addr = proxy_start.accept()

        while True:
            
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_end:
                get_remote_ip(HOST)


main()