import socket
import time

host="127.0.0.1"
port=5000

sock =socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((host,port))

print(f"listening on {host}:{port}")

prev=None
bits=""
started=False

while True:
    data, address = sock.recvfrom(1024)
    current_time = time.monotonic()

    if data==b"START":
        started=True
        continue

    if data==b"SYNC" and started:
        prev=current_time
        continue

    if data==b"END":
        break

    if data==b"DATA" and started:
        delay=current_time-prev

        if delay > 0.15:
            bits+="1"
        else:
            bits+="0"

        prev=current_time

        

print(f"Received bits:{bits}")

message=""

for i in range(0, len(bits), 8):
    byte = bits[i:i + 8]

    if len(byte) < 8:
        break

    message += chr(int(byte, 2))

print("Hidden message:", message)

sock.close()
