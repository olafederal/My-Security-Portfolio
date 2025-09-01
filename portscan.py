#!/usr/bin/env python3
import socket

target = "mgrmgmt.com"
port = (443)


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout (1)

result = sock.connect_ex((target, port))

if result ==0:
   print(f"port {port} is OPEN")
else:
  print(f"port {port} is CLOSED")
sock.close()
