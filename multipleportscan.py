#!/usr/bin/env python3
import socket


target ="10.60.1.26"

start_port = 20
end_port = 3389


print(f"Scanning {target} from port {start_port} to {end_port}...\n")


for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)


    result = sock.connect_ex((target, port))

    if result == 0:
       print(f"port {port} is OPEN")

    else:

        print(f"Port {port} is CLOSE")
    sock.close()


print("\nscan Compleated.")


