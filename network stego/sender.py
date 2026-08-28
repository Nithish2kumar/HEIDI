import socket
import time

host="127.0.0.1"
port=5000

shortD=0.05
longD=0.25

def t2b(msg):
    return "".join(format(ord(char),"08b") for char in msg)

def sendMsg(msg):

    sock =socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bin=t2b(msg)

    print("Message: ",msg)
    print("Bits: ", bin)
    sock.sendto(b"START",(host,port))
    time.sleep(0.5)

    for bit in bin:
        if bit=="0":
            delay=shortD
        else:
            delay=longD

        time.sleep(delay)
        sock.sendto(b"DATA",(host,port))
        print(f"Sent bit: {bit} | Delay: {delay}s")
    time.sleep(0.5)
    sock.sendto(b"END",(host,port))
    sock.close()

    print("Message sent successfully")

mes=input("Enter message: ")
sendMsg(mes)