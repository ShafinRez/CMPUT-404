import socket, time, sys 
from multiprocessing import Process

HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def get_remote_ip(extern_host):
    print(f'Getting IP for {extern_host}')
    try:
        remote_ip = socket.gethostbyname(extern_host)
    except socket.gaierror:
        print ('Hostname could not be resolved. Exiting')
        sys.exit()

    print (f'Ip address of {extern_host} is {remote_ip}')
    return remote_ip

def handle_request():
    
    return


def main():
    HOST = ""
    EXTERN_HOST = 'www.google.com'
    PORT = 8001
    BUFFER_SIZE = 1024
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_start:
        proxy_start.bind((HOST, PORT))
        proxy_start.listen()
        
        while True:
            conn, addr = proxy_start.accept()
            print("Connected by", addr)
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_end:
                ext = get_remote_ip(EXTERN_HOST)
                proxy_end.bind((ext, PORT))

                target = handle_request()


                conn.close()
main()