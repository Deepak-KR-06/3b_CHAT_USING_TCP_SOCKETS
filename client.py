import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('localhost', 8000))

print("Connected to server")

while True:
    msg = input("Client: ")

    s.send(msg.encode())

    if msg.lower() == "exit":
        break

    reply = s.recv(1024).decode()

    if reply.lower() == "exit":
        print("Server disconnected")
        break

    print("Server:", reply)

s.close()