import socket
import time

host="127.0.0.1"
port=5000

sock =socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((host,port))

print(f"listening on {host}:{port}")

prev=None
bits=""

while True:
    data, address = sock.recvfrom(1024)

    current_time = time.monotonic()
    if prev is not None:
        delay=current_time-prev

        if delay > 0.15:
            bits+="1"
        else:
            bits+="0"

    prev=current_time

    if data==b"END":
        break

print(f"Received bits:{bits}")

for i in range(0, len(bits), 8):
    byte = bits[i:i + 8]

    if len(byte) < 8:
        break

    message += chr(int(byte, 2))

print("Hidden message:", message)

sock.close()
