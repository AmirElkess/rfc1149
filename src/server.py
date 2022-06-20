import socket
import threading
import time

ip = "127.0.0.1" #Change to pc's address
tcp_port = 65432
udp_port = 2021
bufferSize = 1024


def start_udp_server():
    # Create a datagram socket
    UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    # Bind to address and ip
    UDPServerSocket.bind((ip, udp_port))
    print("UDP server up and listening; ")
    # Listen for incoming datagrams
    
    while (True): #main loop that echoes messages sent by the client
        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
        message = bytesAddressPair[0]
        address = bytesAddressPair[1]
        #print(f"Received from client <{address}>")
        UDPServerSocket.sendto(message, address)


def start_tcp_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((ip, tcp_port))
        s.listen()
        print("TCP server up and listening; ")
        conn, addr = s.accept()
        with conn:
            #print('TCP: Connected by', addr)
            while True:
                try:
                    data = conn.recv(1024)
                    if not data:
                        #break
                        conn, addr = s.accept()
                    conn.sendall(data)
                except:
                    pass
                
    


if __name__ == '__main__':
    print(f"Server's IP adress: {socket.gethostbyname(socket.gethostname())}")
    t1 = threading.Thread(target=start_udp_server)
    t2 = threading.Thread(target=start_tcp_server)
    t1.start()
    t2.start()
    t1.join()
    t2.join() 
